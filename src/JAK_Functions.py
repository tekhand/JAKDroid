# JAK Droid Project
# Valley View High School Moreno Valley
# Original Author of Adafruit code: Tony DiCola
# License: Public Domain

# Dependencies
from __future__ import division
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import os

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# set up
pin = 4 # pretty sure this pin goes unsed here 
        # besides the set up but I'll leave it here just in case
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

###################################################################
# I don't know anything about the code below & I'm pretty sure    #
# that Josiah Wallace wrote this so I'm just gonna leave it here  #
# if somebody wants to interpret it for me and document it        #
#                                                  -Tim    =D     #
###################################################################

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
#  Servo Range = 175(right) - 575(left)
#  Center: 300(from left) - 475(from right)

rEyeL = 575
rEyeR = 175
rEyeCFL = 300  #Center From Left
rEyeCFR = 475  #Center From Right

# lEyeL-R = 3
#  Servo Range = 200(right) - 550(left)
#  Center: 400(from both ways)

lEyeL = 550
lEyeR = 200
lEyeC = 400

# topEyelid = 4
#  Servo range = 350(open) - 435(closed)

tEyelidO = 350
tEyelidC = 435

# botttomEyelid = 5
#  Servo range = 225(open) - 310(closed)

bEyelidO = 225
bEyelidC = 310

# mouth = 6
#  Servo range = 450(open) - 225(closed)

mouthO = 450
mouthC = 225

# neckL-R = 7
#   Servo Range = 300(right) - 500(left)
#   Center: 400
#   -1 is for numerically decending numbers IE: 400 - 300
#   1 is for numerically ascending numbers IE: 300 - 500
#   To move head left=>right it would be
#      for(neckL, neckR, -1):

neckL = 500
neckC = 400
neckR = 300

# Head up and down is based off of sleep time not servo positions
# Further away from headStop / 414 is faster movement
# Closer to headStop / 414 is slower movement

# headU-D = 8
headUp = 404   #or 403
headStop = 414
headDown = 424

# Functions
def headUpDown():
    pwm.set_pwm(8, 0, headUp)
    sleep(1)
    pwm.set_pwm(8, 0, headStop)
    sleep(1)
    
    pwm.set_pwm(8, 0, headDown)
    sleep(2)
    pwm.set_pwm(8, 0, headStop)
    sleep(1)

    pwm.set_pwm(8, 0, headUp)
    sleep(1)
    pwm.set_pwm(8, 0, headStop)
    sleep(1)

def simpleTest():    
    shakeHead()
    sleep(.5)
    blink()
    sleep(.5)
    blink()
    sleep(.5)
    lookUp()
    blink()
    lookDown()
    lookCFV()
    introduce()
    
# We don't need to know how this works
# it just does and we can call this function 
# whenever we need to
def blink():
    pwm.set_pwm(4, 0, tEyelidC)
    pwm.set_pwm(5, 0, bEyelidC)
    sleep(.15)

    pwm.set_pwm(4, 0, tEyelidO)
    pwm.set_pwm(5, 0, bEyelidO)

# Simplified function which determines head direction
# PREREQUISTE: start and end are using neck variables
# Left => Right (where Left>Center>Right)
def turnHead(start, end):
    dir = 1 if start<end else -1
    for x in range(start, direction, dir)
        pwm.set_pwm(7, 0, x)
        sleep(.005)

def lookLeft():
    pwm.set_pwm(2, 0, rEyeL)
    pwm.set_pwm(3, 0, lEyeL)
    sleep(.5)

def lookRight():
    pwm.set_pwm(2, 0, rEyeR)
    pwm.set_pwm(3, 0, lEyeR)
    sleep(.5)

def lookCFL(): # Look Center From Left
    pwm.set_pwm(2, 0, rEyeCFL)
    pwm.set_pwm(3, 0, lEyeC)
    sleep(.5)

def lookCFR(): # Look Center From Right
    pwm.set_pwm(2, 0, rEyeCFR)
    pwm.set_pwm(3, 0, lEyeC)
    sleep(.5)

def lookUp(): # Look up
    pwm.set_pwm(0, 0, lEyeU)
    pwm.set_pwm(1, 0, rEyeU)
    time.sleep(.5)

def lookDown(): # Look down
    pwm.set_pwm(0, 0, lEyeD)
    pwm.set_pwm(1, 0, rEyeD)
    sleep(.5)

def lookCFV(): # Look Center from Vertical (whatever that means)
    pwm.set_pwm(0, 0, lEyeC)
    pwm.set_pwm(1, 0, rEyeC)
    sleep(.5)

def rollEyes():
    blink()
    pwm.set_pwm(2, 0, rEyeR)
    pwm.set_pwm(3, 0, lEyeR)
    sleep(.2)
    pwm.set_pwm(0, 0, lEyeU)
    pwm.set_pwm(1, 0, rEyeU)
    sleep(.2)
    pwm.set_pwm(2, 0, rEyeL)
    pwm.set_pwm(3, 0, lEyeL)
    sleep(.2)
    pwm.set_pwm(0, 0, lEyeC)
    pwm.set_pwm(1, 0, rEyeC)
    sleep(.2)
    pwm.set_pwm(2, 0, rEyeCFL)
    pwm.set_pwm(3, 0, lEyeC)
    blink()
    sleep(.2)

def shakeHead(): # Shakes head (like how I did at the code I had to document & fix)
    for x in range(400, 300, -1):
        pwm.set_pwm(7, 0, x)
        sleep(.005)
        if x == 350:
            blink()

    for x in range(300, 500, 1):
        pwm.set_pwm(7, 0, x)
        sleep(.005)

    for x in range(500, 300, -1):
        pwm.set_pwm(7, 0, x)
        sleep(.005)
        if x == 430:
            blink()
            
    for x in range(300, 400, 1):
        pwm.set_pwm(7, 0, x)
        sleep(.005)
        if x == 399:
            blink()

# Basic function which commands Jak to open his mouth,
# then speak, then close it again
def say(speakVar):
    pwm.set_pwm(6, 0, 350) # opens mouth
    os.system(("espeak '{}'").format(speakVar)) # takes variable and formats it into espeak
    sleep(.1) # waits in seconds
    pwm.set_pwm(6, 0, 225) # closes mouth
    sleep(.5)

# Interactive functions

# Self explanatory
def introduce():
    say("hello")

    say("My name is Jak")

    say("I am from the mayker space club")

    say("Please join and help me take over the world")

    say("It is now your time to shine")

# Debug: notifies us that everything here ran well.
print('Sucessfully started... press Ctrl-C to quit...')

# Everything here is commented out
# and will be used to debug code

# Main operations
#simpleTest()

# Voice
#introduce()

# Eye movements
#blink()
#lookLeft()
#lookRight()
#lookCFL()
#lookCFR()
#lookUp()
#lookDown()
#lookCFV()
#rollEyes()

# Horizontal Head Rotations
#headLeftFC()
#headLTR()
#headCFR()
#shakeHead()

# Vertical Head Rotations
#headUpDown()
