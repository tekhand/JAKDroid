# JAK Droid Project
# Valley View High School Moreno Valley
# 2017-2018 Lead: Josiah Wallace
# 2017-2018 Team: Kaitlin Hernandez, Kenneth G Sanchez
# 2018-2019 Lead: Kaitlin Hernandez
# 2018-2019 Team: N/A
# 2019-2020 Lead: Timothy Lor
# 2019-2020 Team: Aaron Liam, Roman Lara, Ray Tabelual
# Original Author of Adafruit code: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import RPi.GPIO as GPIO
pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Import the PCA9685 module.
import Adafruit_PCA9685
import os

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# lEyeU-D = 0
#   Servo Range = 390(down) - 440(up)
#   Center: 410

lEyeU = 440
lEyeD = 390
lEyeC = 410

# rEyeU-D = 1
#   Servo Range = 525(down) - 470(up)
#   Center: 510

rEyeU = 470
rEyeD = 525
rEyeC = 510

# rEyeL-R = 2
#   Servo Range = 175(right) - 575(left)
#   Center: 300(from left) - 475(from right)

rEyeL = 575
rEyeR = 175
rEyeCFL = 300  #Center From Left
rEyeCFR = 475  #Center From Right

# lEyeL-R = 3
#   Servo Range = 200(right) - 550(left)
#   Center: 400(from both ways)

lEyeL = 550
lEyeR = 200
lEyeC = 400

# topEyelid = 4
#   Servo range = 350(open) - 435(closed)

tEyelidO = 350
tEyelidC = 435

# botttomEyelid = 5
#   Servo range = 225(open) - 310(closed)

bEyelidO = 225
bEyelidC = 310

# mouth = 6
#   Servo range = 450(open) - 225(closed)

mouthO = 450
mouthC = 225

# neckL-R = 7
#   Servo Range = 300(right) - 500(left)
#   Center: 400
#   -1 is for numerically decreasing numbers IE: 400 - 300
#   1 is for numerically increasing numbers IE: 300 - 500


neckL = 500
neckR = 300
neckC = 400


# Head up and down is based off of sleep time not servo positions
# Further away from headStop / 414 is faster movement
# Closer to headStop / 414 is slower movement

# headU-D = 8
headUp = 404   #or 403
headStop = 414
headDown = 424

#functions
def headUpDown():
    pwm.set_pwm(8, 0, headUp)
    time.sleep(1)
    pwm.set_pwm(8, 0, headStop)
    time.sleep(1)
    
    pwm.set_pwm(8, 0, headDown)
    time.sleep(2)
    pwm.set_pwm(8, 0, headStop)
    time.sleep(1)

    pwm.set_pwm(8, 0, headUp)
    time.sleep(1)
    pwm.set_pwm(8, 0, headStop)
    time.sleep(1)

def s():    #Sleep
    time.sleep(.5)

def simpleTest():
        
    shakeHead();
    s();
    blink();
    s();
    blink();
    s();
    lookUp();
    blink();
    lookDown();
    lookCFV();
    introduceJak();
    

def blink():
    pwm.set_pwm(4, 0, tEyelidC)
    pwm.set_pwm(5, 0, bEyelidC)
    time.sleep(.15)

    pwm.set_pwm(4, 0, tEyelidO)
    pwm.set_pwm(5, 0, bEyelidO)

def headLeftFC():
    for x in range(400, 500, 1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)

def headCFL():
    for x in range(500, 400, -1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
def headRightFC():
    for x in range(400, 300, -1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
def headCFR():
    for x in range(300, 400, 1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
def headLTR(): # head left to right
     for x in range(500, 300, -1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
def headRTL(): # head right to left
    for x in range(300, 500, 1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)




def lookLeft():
    pwm.set_pwm(2, 0, rEyeL)
    pwm.set_pwm(3, 0, lEyeL)
    time.sleep(.5)

def lookRight():
    pwm.set_pwm(2, 0, rEyeR)
    pwm.set_pwm(3, 0, lEyeR)
    time.sleep(.5)

def lookCFL():
    pwm.set_pwm(2, 0, rEyeCFL)
    pwm.set_pwm(3, 0, lEyeC)
    time.sleep(.5)

def lookCFR():
    pwm.set_pwm(2, 0, rEyeCFR)
    pwm.set_pwm(3, 0, lEyeC)
    time.sleep(.5)

def lookUp():
    pwm.set_pwm(0, 0, lEyeU)
    pwm.set_pwm(1, 0, rEyeU)
    time.sleep(.5)

def lookDown():
    pwm.set_pwm(0, 0, lEyeD)
    pwm.set_pwm(1, 0, rEyeD)
    time.sleep(.5)

def lookCFV(): #Center from Vertical
    pwm.set_pwm(0, 0, lEyeC)
    pwm.set_pwm(1, 0, rEyeC)
    time.sleep(.5)

def rollEyes():
    blink();
    pwm.set_pwm(2, 0, rEyeR)
    pwm.set_pwm(3, 0, lEyeR)
    time.sleep(.2)
    pwm.set_pwm(0, 0, lEyeU)
    pwm.set_pwm(1, 0, rEyeU)
    time.sleep(.2)
    pwm.set_pwm(2, 0, rEyeL)
    pwm.set_pwm(3, 0, lEyeL)
    time.sleep(.2)
    pwm.set_pwm(0, 0, lEyeC)
    pwm.set_pwm(1, 0, rEyeC)
    time.sleep(.2)
    pwm.set_pwm(2, 0, rEyeCFL)
    pwm.set_pwm(3, 0, lEyeC)
    blink();
    s();

def shakeHead():
    for x in range(400, 300, -1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
        if x == 350:
            blink();

    for x in range(300, 500, 1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)

    for x in range(500, 300, -1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
        if x == 430:
            blink();
            
    for x in range(300, 400, 1):
        pwm.set_pwm(7, 0, x)
        time.sleep(.005)
        if x == 399:
            blink();
            
def speak(speakVar):
    pwm.set_pwm(6, 0, 350) #opens mouth
    os.system(("espeak '{}'").format(speakVar))
    time.sleep(.1) #waits in seconds
    pwm.set_pwm(6, 0, 225) #closes mouth
    time.sleep(.5)

#only documenting this functions cause why not
def introduceJak():

    speak("hello")

    speak("My name is Jak")

    speak("I am from the mayker space club")

    speak("Please join and help me take over the world")

    speak("It is now your time to shine")
    

def talkToStudent():
    #That's whos name?
    pwm.set_pwm(6, 0, 350)
    os.system("espeak 'Students")
    time.sleep(.1)
    pwm.set_pwm(6, 0, 225)
    #That's whos name?
    pwm.set_pwm(6, 0, 350)
    os.system("espeak 'My Name is Jak'")
    time.sleep(.1)
    pwm.set_pwm(6, 0, 225)
    time.sleep(.1)
    pwm.set_pwm(6, 0, 350)
    os.system("espeak 'Valley View High School Cybor student'")
    time.sleep(.1)
    pwm.set_pwm(6, 0, 225)


print('Sucessfully started... press Ctrl-C to quit...')

#start everything for debugging
#time.sleep(.5)

#main operations
#headUpDown();
#simpleTest();
#blink();
#shakeHead();
#talkToStudent();
#introduceJak();
#skit();

#head movements
#lookLeft();
#lookRight();
#lookCFL();
#lookCFR();
#lookUp();
#lookDown();
#lookCFV();

# collaborate eyes
#rollEyes();

#headLeftFC();
#headLTR();
#headCFR();
           
