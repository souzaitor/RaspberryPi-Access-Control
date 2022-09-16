import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

## Set Hardware GPIO pins
RS = 18
EN = 23
D4 = 24
D5 = 25
D6 = 8
D7 = 7
enrol_button = 5
delete_button = 6
increase_button = 13
decrease_button = 19
led = 26

# 
HIGH = 1
LOW = 0

#
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(RS, gpio.OUT)
gpio.setup(EN, gpio.OUT)
gpio.setup(D4, gpio.OUT)
gpio.setup(D5, gpio.OUT)
gpio.setup(D6, gpio.OUT)
gpio.setup(D7, gpio.OUT)
gpio.setup(enrol_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(delete_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(increase_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(decrease_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(led, gpio.OUT)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword()  ==  False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)

def begin():
    lcdcmd(0x33) 
    lcdcmd(0x32) 
    lcdcmd(0x06)
    lcdcmd(0x0C) 
    lcdcmd(0x28) 
    lcdcmd(0x01) 
    time.sleep(0.0005)
 
def lcdcmd(ch): 
    gpio.output(RS, 0)
    gpio.output(D4, 0)
    gpio.output(D5, 0)
    gpio.output(D6, 0)
    gpio.output(D7, 0)

    if ch & 0x10 == 0x10:
        gpio.output(D4, 1)
    if ch & 0x20 == 0x20:
        gpio.output(D5, 1)
    if ch & 0x40 == 0x40:
        gpio.output(D6, 1)
    if ch & 0x80 == 0x80:
        gpio.output(D7, 1)

    gpio.output(EN, 1)
    time.sleep(0.005)
    gpio.output(EN, 0)

    # Low bits
    gpio.output(D4, 0)
    gpio.output(D5, 0)
    gpio.output(D6, 0)
    gpio.output(D7, 0)
    if ch & 0x01 == 0x01:
        gpio.output(D4, 1)
    if ch & 0x02 == 0x02:
        gpio.output(D5, 1)
    if ch & 0x04 == 0x04:
        gpio.output(D6, 1)
    if ch & 0x08 == 0x08:
        gpio.output(D7, 1)
    gpio.output(EN, 1)
    time.sleep(0.005)
    gpio.output(EN, 0)
  
def LCD_write(ch): 
    gpio.output(RS, 1)
    gpio.output(D4, 0)
    gpio.output(D5, 0)
    gpio.output(D6, 0)
    gpio.output(D7, 0)

    if ch & 0x10 == 0x10:
        gpio.output(D4, 1)
    if ch & 0x20 == 0x20:
        gpio.output(D5, 1)
    if ch & 0x40 == 0x40:
        gpio.output(D6, 1)
    if ch & 0x80 == 0x80:
        gpio.output(D7, 1)

    gpio.output(EN, 1)
    time.sleep(0.005)
    gpio.output(EN, 0)
    
    # Low bits
    gpio.output(D4, 0)
    gpio.output(D5, 0)
    gpio.output(D6, 0)
    gpio.output(D7, 0)

    if ch & 0x01 == 0x01:
        gpio.output(D4, 1)
    if ch & 0x02 == 0x02:
        gpio.output(D5, 1)
    if ch & 0x04 == 0x04:
        gpio.output(D6, 1)
    if ch & 0x08 == 0x08:
        gpio.output(D7, 1)

    gpio.output(EN, 1)
    time.sleep(0.005)
    gpio.output(EN, 0)

def LCD_clear():
    lcdcmd(0x01)
 
def LCD_print(string):
    l = 0
    l = len(string)

    for i in range(l):
        LCD_write(ord(string[i]))
    
def setCursor(x,y):
    if y  ==  0:
        n=128+x
    elif y  ==  1:
        n=192+x
    lcdcmd(n)


def enroll_finger():
    """

    """
    lcdcmd(1)
    LCD_print("Cadastrando digital")
    time.sleep(2)
    print('Waiting for finger...')
    lcdcmd(1)
    LCD_print("Place Finger")
    while ( f.readImage()  ==  False ):
        pass
    
    f.convertImage(0x01)
    result = f.searchTemplate()
    position_number = result[0]

    if ( position_number >= 0 ):
        print('Template already exists at position #' + str(position_number))
        
        # LCD print message
        lcdcmd(1)
        LCD_print("Finger Already")
        lcdcmd(192)
        LCD_print("   Exists     ")
        
        time.sleep(2)
        return
    
    print('Remove finger...')
    lcdcmd(1)
    LCD_print("Remove Finger")
    time.sleep(2)

    print('Waiting for same finger again...')
    lcdcmd(1)
    LCD_print("Place Finger")
    lcdcmd(192)
    LCD_print("   Again    ")
    while ( f.readImage()  ==  False ):
        pass
    f.convertImage(0x02)

    if ( f.compareCharacteristics()  ==  0 ):
        print ("Fingers do not match")
        lcdcmd(1)
        LCD_print("Finger Did not")
        lcdcmd(192)
        LCD_print("   Mactched   ")
        time.sleep(2)
        return
    
    f.createTemplate()
    position_number = f.storeTemplate()

    print('Finger enrolled successfully!')
    print('New template position #' + str(position_number))

    lcdcmd(1)
    LCD_print("Stored at Pos:")
    LCD_print(str(position_number))
    lcdcmd(192)
    LCD_print("successfully")

    time.sleep(2)

def searchFinger():
    try:
        print('Waiting for finger...')
        while( f.readImage()  ==  False ):
            #pass
            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        position_number = result[0]
        accuracyScore = result[1]
        if position_number  ==  -1 :
            print('No match found!')
            lcdcmd(1)
            LCD_print("No Match Found")
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(position_number))
            lcdcmd(1)
            LCD_print("Found at Pos:")
            LCD_print(str(position_number))
            time.sleep(2)
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
    
def deleteFinger():
    """
    
    """
    position_number = 0
    count=0
    lcdcmd(1)
    LCD_print("Delete Finger")
    lcdcmd(192)
    LCD_print("Position: ")
    lcdcmd(0xca)
    LCD_print(str(count))

    while gpio.input(enrol_button)  ==  True:   # here enrol_button key means ok
        if gpio.input(increase_button)  ==  False:
            count=count+1
            if count>1000:
                count=1000
            lcdcmd(0xca)
            LCD_print(str(count))
            time.sleep(0.2)
        elif gpio.input(decrease_button)  ==  False:
            count=count-1
            if count<0:
                count=0
            lcdcmd(0xca)
            LCD_print(str(count))
            time.sleep(0.2)
    position_number=count
    if f.deleteTemplate(position_number)  ==  True :
        print('Template deleted!')
        lcdcmd(1)
        LCD_print("Finger Deleted");
        time.sleep(2)
begin()
lcdcmd(0x01)
LCD_print("FingerPrint ")
lcdcmd(0xc0)
LCD_print("Interfacing ")
time.sleep(3)
lcdcmd(0x01)
LCD_print("Circuit Digest")
lcdcmd(0xc0)
LCD_print("Welcomes You  ")
time.sleep(3)
flag=0
LCD_clear()
while 1:
    gpio.output(led, HIGH)
    lcdcmd(1)
    LCD_print("Place Finger")
    if gpio.input(enrol_button)  ==  0:
        gpio.output(led, LOW)
        enroll_finger()
    elif gpio.input(delete_button)  ==  0:
        gpio.output(led, LOW)
        while gpio.input(delete_button)  ==  0:
            time.sleep(0.1)
        deleteFinger()
    else:
        searchFinger()
