import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor

motor1 = motor.motorbk(7)
print(motor1.read())
