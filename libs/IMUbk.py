import wirebk
import time
import const
import struct
Define = const._const()

##chip ina226
Define.SLAVE_ADDRESS_IMU=0x68
Define.SLAVE_ADDRESS_MAG = 0x0C

Define.ACCEL_RESOLUTION = 4
Define.GYRO_RESOLUTION = 500

Define.MAG_RESOLUTION = 4912 # uteslas



class IMUbk(object):
    ##variables estaticas aqui
    ##sensor_declared=0
    imudata = [0]*9
    magsensitivity = [0]*3
    
    
    def __init__(self):
        #configure gyroscope range
        wirebk.WriteBk(Define.SLAVE_ADDRESS_IMU, 27, 0x08) #500 dps
        #configure accelerometer range
        wirebk.WriteBk(Define.SLAVE_ADDRESS_IMU, 28, 0x08) #+-4g
        #Set by pass mode for the magnetometer
        wirebk.WriteBk(Define.SLAVE_ADDRESS_IMU, 0x37, 0x02)

        # Magnetometer configuration
        wirebk.WriteBk(Define.SLAVE_ADDRESS_MAG, 0x0A, 0x00) # power down magnetometer
        time.sleep(.01)
        wirebk.WriteBk(Define.SLAVE_ADDRESS_MAG, 0x0A, 0x0F) # fuse ROM access mode
        time.sleep(.01)
        self.magsensitivity = wirebk.ReadBk2(Define.SLAVE_ADDRESS_MAG, 3, 0x10) # Read mag sensitivity values

        self.magsensitivity[0] = ((self.magsensitivity[0] - 128)/256) + 1
        self.magsensitivity[1] = ((self.magsensitivity[1] - 128)/256) + 1
        self.magsensitivity[2] = ((self.magsensitivity[2] - 128)/256) + 1
        
        wirebk.WriteBk(Define.SLAVE_ADDRESS_MAG, 0x0A, 0x00) # power down magnetometer
        time.sleep(.01)
        
        # 0x16 Continuous measurement mode 2 (100 Hz) and 16 bit mode
        # 0x12 Continuous measurement mode 1 (8 Hz) and 16 bit mode
        wirebk.WriteBk(Define.SLAVE_ADDRESS_MAG, 0x0A, 0x16)
 
        time.sleep(.01)
        
        
        
    ##this function return number of milliwatts(25mW por bit)
    def read(self):
        raw = wirebk.ReadBk2(Define.SLAVE_ADDRESS_IMU, 14, 0x3B) # read 14 bytes starting at 0x3B
        self.imudata[0] = struct.unpack(">h", bytes(raw[0:2]))[0] / 32768 * Define.ACCEL_RESOLUTION #X
        self.imudata[1] = struct.unpack(">h", bytes(raw[2:4]))[0] / 32768 * Define.ACCEL_RESOLUTION #Y
        self.imudata[2] = struct.unpack(">h", bytes(raw[4:6]))[0] / 32768 * Define.ACCEL_RESOLUTION #Z

        self.imudata[3] = struct.unpack(">h", bytes(raw[8:10]))[0] / 32768 * Define.GYRO_RESOLUTION #X
        self.imudata[4] = struct.unpack(">h", bytes(raw[10:12]))[0] / 32768 * Define.GYRO_RESOLUTION #Y
        self.imudata[5] = struct.unpack(">h", bytes(raw[12:14]))[0] / 32768 * Define.GYRO_RESOLUTION #Z

        magraw = wirebk.ReadBk2(Define.SLAVE_ADDRESS_MAG, 8, 0x02) # Read mag values
        if(int(magraw[0]) & 0b1):
            if(not(magraw[7] & 0x08)):
                #print(magraw)
                
                self.imudata[6] = struct.unpack("<h", bytes(magraw[1:3]))[0] * self.magsensitivity[0]
                self.imudata[7] = struct.unpack("<h", bytes(magraw[3:5]))[0] * self.magsensitivity[1]
                self.imudata[8] = struct.unpack("<h", bytes(magraw[5:7]))[0] * self.magsensitivity[2]

                self.imudata[6] = self.imudata[6] / 32760 * Define.MAG_RESOLUTION
                self.imudata[7] = self.imudata[7] / 32760 * Define.MAG_RESOLUTION
                self.imudata[8] = self.imudata[8] / 32760 * Define.MAG_RESOLUTION
                
                #self.imudata[7] = struct.unpack("<h", bytes(raw[1:3]))[0] / 32768 * Define.MAG_RESOLUTION #X
                #self.imudata[6] = struct.unpack("<h", bytes(raw[3:5]))[0] / 32768 * Define.MAG_RESOLUTION #Y
                #self.imudata[8] = struct.unpack("<h", bytes(raw[5:7]))[0] * -1 / 32768 * Define.MAG_RESOLUTION #Z

                #self.imudata[6] = struct.unpack("<h", bytes(magraw[1:3]))[0]
                #self.imudata[7] = struct.unpack("<h", bytes(magraw[3:5]))[0]
                #self.imudata[8] = struct.unpack("<h", bytes(magraw[5:7]))[0]
            
        return(self.imudata)

        
