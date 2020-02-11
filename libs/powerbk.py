import wirebk
import time
import const
Define = const._const()

##chip ina226
Define.SLAVE_ADDRESS_POWERMODULE=0x40

Define.REGISTER_CONFIGURATION = 0X00
Define.REGISTER_SHUNREGISTER= 0X01
Define.REGISTER_BUSVOLTAGE = 0X02
Define.REGISTER_CALIBRATION = 0X05
Define.REGISTER_CURRENT = 0X04
Define.REGISTER_POWER = 0X03


class powerbk(object):
    ##variables estaticas aqui
    ##sensor_declared=0
    
    def __init__(self):
        wirebk.WriteBk(Define.SLAVE_ADDRESS_POWERMODULE,Define.REGISTER_CONFIGURATION,[0x44,0xDF])
        calibrationvar = 1024  ##1ma por bit
        highbyte= calibrationvar>>8 & 0xff
        lowbyte=  calibrationvar & 0xff
        error_com = wirebk.WriteBk(Define.SLAVE_ADDRESS_POWERMODULE,Define.REGISTER_CALIBRATION,[highbyte,lowbyte])
        if(error_com =="error"):
            print("Error in power sensor initialization")
        
        
    ##this function return number of milliampers(1mA por bit)
    def readcurrent(self):
        sensorval="error"
        #wirebk.WriteBk1byte(Define.SLAVE_ADDRESS_POWERMODULE,Define.REGISTER_CURRENT)
        sensorval = wirebk.ReadBk2(Define.SLAVE_ADDRESS_POWERMODULE,2,Define.REGISTER_CURRENT)
        if(sensorval[0]=="error"):
            print("power sensor {} not working".format(self.portnum))
        else:
            sensorval = sensorval[0] << 8 | sensorval[1]
        return(sensorval)

    ##this function return number of millivolts (1.25mV por bit)
    def readvoltage(self):
        sensorval="error"
        #wirebk.WriteBk1byte(Define.SLAVE_ADDRESS_POWERMODULE,Define.REGISTER_BUSVOLTAGE)
        sensorval = wirebk.ReadBk2(Define.SLAVE_ADDRESS_POWERMODULE,2,Define.REGISTER_BUSVOLTAGE)
        if(sensorval[0]=="error"):
            print("power sensor {} not working".format(self.portnum))
        else:
            sensorval = sensorval[0] << 8 | sensorval[1]
        return(sensorval*1.25)

    ##this function return number of milliwatts(25mW por bit)
    def readpower(self):
        sensorval="error"
        #wirebk.WriteBk1byte(Define.SLAVE_ADDRESS_POWERMODULE,Define.REGISTER_POWER)
        sensorval = wirebk.ReadBk2(Define.SLAVE_ADDRESS_POWERMODULE,2,Define.REGISTER_POWER)
        if(sensorval[0]=="error"):
            print("power sensor {} not working".format(self.portnum))
        else:
            sensorval = sensorval[0] << 8 | sensorval[1]
        return(sensorval*25)

        
