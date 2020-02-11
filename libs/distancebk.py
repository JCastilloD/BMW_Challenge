import wirebk
import time
import const
Define = const._const()

Define.SLAVE_ADDRESS_ULTRASONIC=0x60

class distancebk(object):
    ##variables estaticas aqui
    ##sensor_declared=0
    
    def __init__(self,portnum=0):
        self.portnum = portnum

    def read(self):
        distance="error"
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            distance = wirebk.ReadBk(Define.SLAVE_ADDRESS_ULTRASONIC,1)[0]
            if(distance=="error"):
                print("distance sensor {} not working".format(self.portnum))
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)
        time.sleep(0.05)
        return(distance)

        
