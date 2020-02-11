import wirebk
import time
import const
import struct
Define = const._const()

Define.SLAVE_ADDRESS_MOTOR=0x5D

Define.REGISTER_DIRECTION_SPEED=0x01
Define.REGISTER_MODE=0x03
Define.REGISTER_BUSY=0x04
Define.READ_ENCODER=0x05
Define.P_GAIN_HI = 0X09
Define.I_GAIN_HI = 0X0B
Define.D_GAIN_HI = 0X0D
Define.DEAD_BAND = 0X0F
Define.REGISTER_MAX_PWM_POS=0x10
Define.REGISTER_POS_VALUE=0x12
Define.REGISTER_COUNT_PER_TURN=0x16
Define.REGISTER_ADDRESS_POINTER=0x1C


class motorbk(object):
    ##variables estaticas aqui
    ##sensor_declared=0
    
    def __init__(self,portnum=0):
        self.portnum = portnum

    def set(self,velocity):
        if(velocity>255):
            velocity=255
        if(velocity<-255):
            velocity=-255
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            velocity = int(velocity)
            highbyte= velocity>>8 & 0xff
            lowbyte=  velocity & 0xff
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_MAX_PWM_POS,0xff)
            statusvar = wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_DIRECTION_SPEED,[highbyte,lowbyte])
            if(statusvar=="error"):
                print("motor {} not working".format(self.portnum))
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)

    ###para mover ciertos grados
    def move(self,velocity,degrees):
        if(velocity>255):
            velocity=255
        if(velocity<-255):
            velocity=-255
        if(velocity<0):
            velocity=velocity*-1
            degrees=degrees*-1
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_ADDRESS_POINTER,Define.REGISTER_COUNT_PER_TURN)
            pulses = wirebk.ReadBk(Define.SLAVE_ADDRESS_MOTOR,2)
            if(pulses[0]!="error"):
                pulsesjoin = pulses[0]<<8 | pulses[1]
                velocity = int(velocity)
                velocity=  velocity & 0xff
                degrees = int((degrees*pulsesjoin)/360)
                data_degrees = [degrees>>24 & 0xff,degrees>>16 & 0xff,degrees>>8 & 0xff,degrees & 0xff]
                wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_MAX_PWM_POS,velocity)
                wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_POS_VALUE,data_degrees)
            else:
                print("motor {} not working".format(self.portnum))
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)

    ###para mover vueltas
    def turn(self,velocity,revolutions):
        self.move(velocity,revolutions*360)

    ###para esperar a que acabe
    def wait(self):
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            statusvar=1
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_ADDRESS_POINTER,Define.REGISTER_BUSY)
            while(statusvar==1):
                statusvar=wirebk.ReadBk(Define.SLAVE_ADDRESS_MOTOR,1)[0]
                time.sleep(0.01)
            if(statusvar=="error"):
                print("motor {} not working".format(self.portnum))
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)

    def read(self):
        sensordata="error"
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.REGISTER_ADDRESS_POINTER,Define.READ_ENCODER)
            sensordata = wirebk.ReadBk(Define.SLAVE_ADDRESS_MOTOR,4)
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)
        if(sensordata[0]=="error"):
            print("distance sensor {} not working".format(self.portnum))
            return(sensordata)
        else:
           return(struct.unpack(">i", bytes(sensordata))[0]) 

    def configPID(self,P_val,I_val,D_val,dead_band):
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            highbyte= P_val>>8 & 0xff
            lowbyte=  P_val & 0xff
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.P_GAIN_HI,[highbyte,lowbyte])
            highbyte= I_val>>8 & 0xff
            lowbyte=  I_val & 0xff
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.I_GAIN_HI,[highbyte,lowbyte])
            highbyte= D_val>>8 & 0xff
            lowbyte=  D_val & 0xff
            wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.D_GAIN_HI,[highbyte,lowbyte])
            highbyte= dead_band>>8 & 0xff
            lowbyte=  dead_band & 0xff
            statusvar = wirebk.WriteBk(Define.SLAVE_ADDRESS_MOTOR,Define.DEAD_BAND,[highbyte,lowbyte])
            if(statusvar=="error"):
                print("motor {} not working".format(self.portnum))
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)
