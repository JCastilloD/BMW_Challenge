import sys
sys.path.append("/home/pi/bmw/libs")
import distancebk as distance

sensor = distance.distancebk(3)
print(sensor.read())
