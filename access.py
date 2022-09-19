import time
from pyfingerprint.pyfingerprint import PyFingerprint
import hashlib
from RPLCD import CharLCD
import RPi.GPIO as GPIO

# Initialize pins
pin_rs = 12
pin_en = 16
pin_D4 = 18
pin_D5 = 22
pin_D6 = 24
pin_D7 = 26
#pin_buzzer = 2
#pin_relay = 1

# Initialize LCD
lcd = CharLCD(cols=16, rows=2, pin_rs=pin_rs, pin_e=pin_en, pins_data=[18, 22, 24, 26], numbering_mode=GPIO.BOARD)

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin_buzzer, GPIO.OUT)
#GPIO.setup(pin_relay,  GPIO.OUT)


def delete_finger():
    """
    Delete the template of the finger
    """
    try:
        positionNumber = input('Please enter the template position you want to delete: ')
        lcd.write_string(u'Enter template to delete:')
        positionNumber = int(positionNumber)

        if ( f.deleteTemplate(positionNumber) == True ):
            print('Template deleted!')
            lcd.write_string(u'Template deleted!')

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        lcd.write_string(u'Operation failed!')
        exit(1)

def search_finger():
    """
    Search the finger and calculate hash
    """
    try:
        lcd.write_string(u'Waiting for finger...')
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('No match found!')
            lcd.write_string(u'Access Denied!')
            exit(0)

        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))

            lcd.write_string(u'Access Allowed')

            # Buzzer beep and Aativate relay 
            GPIO.output(pin_buzzer, GPIO.HIGH)
            GPIO.output(pin_relay, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(pin_buzzer, GPIO.LOW)
            GPIO.output(pin_relay, GPIO.LOW)

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        lcd.write_string(u'Operation failed!')
        exit(1)

def enroll_finger():
    """
    Enrolls new finger
    """
    ## Tries to enroll new finger
    try:
        print('Waiting for finger...')
        lcd.write_string(u'Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            lcd.write_string(u'Template already exists at pos ' + str(positionNumber))
            exit(0)

        print('Remove finger...')
        lcd.write_string(u'Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')
        lcd.write_string(u'Waiting for same finger again...')

        ## Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        ## Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Fingers do not match')

        ## Creates a template
        f.createTemplate()

        ## Saves template at new position number
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))
        lcd.write_string(u'Finger enrolled successfully! Pos# '+ str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)


if __name__ == "__main__":
    ## Initialize fingerprint sensor
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        lcd.write_string(u"fingerprint sensor error")
        exit(1)

    while True:
        search_finger()