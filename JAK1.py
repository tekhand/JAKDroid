# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

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
#   Servo Range = 380(down) - 440(up)
#   Center: 410

# rEyeU-D = 1
#   Servo Range = #535(down) - 480(up)
#   Center: 510

# rEyeL-R = 2

# lEyeL-R = 3

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
    
    for x in range(0, 3):
        
        pwm.set_pwm(7, 0, 350)
        time.sleep(1)
        pwm.set_pwm(7, 0, 500)
        time.sleep(1)
        pwm.set_pwm(7, 0, 400)
        time.sleep(1)

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


print('press Ctrl-C to quit...')
    
#headUpDown();
#simpleTest();
pwm.set_pwm(0, 0, 410)
pwm.set_pwm(1, 0, 510)
