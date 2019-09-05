# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

import os

def word(something):
    os.system('espeak -s200 -ven "{0}"' .format(something))

def say(text):
    mouthSpeed = 0.15
    mouthClose = 250
    mouthOpen = 400
    
    pwm.set_pwm(6, 0, mouthClose)
    
    words = text.split()
    print(words)
    for nextWord in words:
        pwm.set_pwm(6, 0, mouthOpen)
        word(nextWord)
        pwm.set_pwm(6, 0, mouthClose)
        time.sleep(mouthSpeed)

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
neckRight = 325  # Min pulse length out of 4096
neckLeft = 425  # Max pulse length out of 4096

eyeLidBottomPin = 5
# Configure min and max servo pulse lengths
eyeLidBotUp = 320
eyeLidBotDown =  230

mouthPin = 6

# Configure min and max servo pulse lengths
mouthUp = 225
mouthDown = 450

neckRightLeftPin = 7
# Configure min and max servo pulse lengths
neckRight = 325  # Min pulse length out of 4096
neckLeft = 425  # Max pulse length out of 4096

headUpDownPin = 8
headUp = 400
headStop = 413
headDown = 424


# lEyeU-D = 0
#   Servo Range = 390(down) - 440(up)
#   Center: 410

# rEyeU-D = 1
#   Servo Range = 525(down) - 470(up)
#   Center: 510

# rEyeL-R = 2
#   Servo Range = 175(right) - 575(left)
#   Center: 300(from left) - 475(from right)

# lEyeL-R = 3
#   Servo Range = 200(right) - 550(left)
#   Center: 400(from both ways)

# topEyelid = 4
#   Servo range = 350(open) - 435(closed)

# botttomEyelid = 5
#   Servo range = 225(open) - 310(closed)

# mouth = 6

# neckL-R = 7

# headU-D = 8

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

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

def simpleTest():
    
    for x in range(0, 1):
        
        #neckR-L
        for x in range(400, 300, -1):
            pwm.set_pwm(7, 0, x)
            time.sleep(.005)

        for x in range(300, 500, 1):
            pwm.set_pwm(7, 0, x)
            time.sleep(.005)

        for x in range(500, 300, -1):
            pwm.set_pwm(7, 0, x)
            time.sleep(.005)

        for x in range(300, 400, 1):
            pwm.set_pwm(7, 0, x)
            time.sleep(.005)
        
        #eyelid
        pwm.set_pwm(4, 0, 435)
        pwm.set_pwm(5, 0, 310)
        time.sleep(.15)

        pwm.set_pwm(4, 0, 350)
        pwm.set_pwm(5, 0, 225)
        time.sleep(1)

        pwm.set_pwm(4, 0, 435)
        pwm.set_pwm(5, 0, 310)
        time.sleep(.15)

        pwm.set_pwm(4, 0, 350)
        pwm.set_pwm(5, 0, 225)
        time.sleep(1)

        #eyesU
        pwm.set_pwm(0, 0, 440)
        pwm.set_pwm(1, 0, 470)
        time.sleep(.2)

        #blink
        pwm.set_pwm(4, 0, 435)
        pwm.set_pwm(5, 0, 310)
        time.sleep(.15)


        pwm.set_pwm(4, 0, 350)
        pwm.set_pwm(5, 0, 225)
        time.sleep(.2)

        #eyesD
        pwm.set_pwm(0, 0, 390)
        pwm.set_pwm(1, 0, 525)
        time.sleep(1)
        
        #eyesC
        pwm.set_pwm(0, 0, 410)
        pwm.set_pwm(1, 0, 510)
        time.sleep(1)

        #eyesR-L
        pwm.set_pwm(2, 0, 175)
        pwm.set_pwm(3, 0, 200)
        time.sleep(1)

        pwm.set_pwm(2, 0, 575)
        pwm.set_pwm(3, 0, 550)
        time.sleep(1)

        pwm.set_pwm(2, 0, 300)
        pwm.set_pwm(3, 0, 400)
        time.sleep(1)
        


print('press Ctrl-C to quit...')

espeak("test")
pwm.set_pwm(2, 0, 175)
pwm.set_pwm(3, 0, 200)
time.sleep(1)
pwm.set_pwm(2, 0, 300)
pwm.set_pwm(3, 0, 400)
time.sleep(1)
say("Hi")
