import sys
sys.path.append("/home/pi/bmw/libs")
import powerbk as power

powerS = power.powerbk()
print(powerS.readvoltage())
