import time
from pyfingerprint.pyfingerprint import PyFingerprint
import hashlib
from RPLCD import CharLCD
import RPi.GPIO as GPIO
import requests

# Initialize pins
pin_rs = 12
pin_en = 16
pin_D4 = 18
pin_D5 = 22
pin_D6 = 24
pin_D7 = 26
pin_buzzer = 37
pin_relay = 3

# Initialize LCD
lcd = CharLCD(cols=16, rows=2, pin_rs=pin_rs, pin_e=pin_en, pins_data=[18, 22, 24, 26], numbering_mode=GPIO.BOARD)
lcd.clear()

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_buzzer, GPIO.OUT)
GPIO.setup(pin_relay,  GPIO.OUT)
GPIO.output(pin_relay, GPIO.LOW)
GPIO.output(pin_buzzer, GPIO.LOW)


def search_finger():
    """
    Search the finger and calculate hash
    """
    try:
        lcd.clear()
        lcd.write_string('Waiting for finger...')
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

            # Makes requisition to access server
            r = requests.get('https://bipes.net.br/acesso_dc/finger.php?card='+str(positionNumber)+'&finger=1')
            print('Request access to server: ' + r.text)

            lcd.clear()
            lcd.write_string('Access Denied!')
            time.sleep(2)
            lcd.clear()

        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))

            # Makes requisition to access server
            r = requests.get('https://bipes.net.br/acesso_dc/finger.php?card='+str(positionNumber)+'&finger=1')
            print('Request access to server: ' + r.text)

            lcd.clear()
            lcd.write_string('Access Allowed')
            
            # Buzzer beep and Activate relay 
            GPIO.output(pin_buzzer, GPIO.HIGH)
            GPIO.output(pin_relay, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(pin_buzzer, GPIO.LOW)
            GPIO.output(pin_relay, GPIO.LOW)

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        lcd.clear()
        lcd.write_string('Operation failed!')
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
        lcd.clear()
        lcd.write_string("fingerprint sensor error")
        exit(1)

    try:
        while True:
            search_finger()
    except KeyboardInterrupt:
        print("Finished")
        lcd.clear()