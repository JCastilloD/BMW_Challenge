import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor
import time

motor1 = motor.motorbk(7)
motor1.set(255)
time.sleep(1)
motor1.set(-255)
time.sleep(1)
motor1.set(0)
