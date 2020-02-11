import sys
sys.path.append("/home/pi/bmw/libs")
import colorbk as colorx
import time

sensor = colorx.colorbk(1)
print("start")
time.sleep(1)
sensor.set("white")
time.sleep(2)
sensor.set("black")
print("end")
