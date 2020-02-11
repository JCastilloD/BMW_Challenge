import sys
sys.path.append("/home/pi/bmw/libs")
import colorbk as colorx

sensor = colorx.colorbk(1)
print(sensor.read("white2"))
