import sys
sys.path.append("/home/pi/bmw/libs")
import IMUbk as IMU

imu = IMU.IMUbk()
print(imu.read())
