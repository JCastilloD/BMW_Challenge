import wirebk
import time
import const
Define = const._const()

Define.SLAVE_ADDRESS_COLORSENSOR=0x7E

Define.REGISTER_ADDR_POINTER=0x00
Define.REGISTER_ENTER_BOOTLOADER=0x01
Define.REGISTER_WRITE_EEPROM=0x02
Define.REGISTER_RESTORE_DEFAULTS=0x03
Define.REGISTER_MODE=0x04
Define.REGISTER_RED=0x05
Define.REGISTER_GREEN=0x06
Define.REGISTER_BLUE=0x07
Define.REGISTER_AMBIENT=0x08
Define.REGISTER_SCALED_RED=0x09
Define.REGISTER_SCALED_GREEN=0x0A
Define.REGISTER_SCALED_BLUE=0x0B
Define.REGISTER_HUE=0x0C
Define.REGISTER_SATURATION=0x0E
Define.REGISTER_VALUE=0x0F
Define.REGISTER_COLOR=0x10
Define.REGISTER_START_CAL=0x11

Define.REGISTER_SOFTWARE_VER=0xC0
Define.REGISTER_HARDWARE_VER=0xC1
Define.REGISTER_CAL_WHITE_R=0xC2
Define.REGISTER_CAL_WHITE_G=0xC3
Define.REGISTER_CAL_WHITE_B=0xC4
Define.REGISTER_CAL_BLACK_R=0xC5
Define.REGISTER_CAL_BLACK_G=0xC6
Define.REGISTER_CAL_BLACK_B=0xC7
Define.REGISTER_SAT_WHITE=0xC8
Define.REGISTER_VALUE_BLACK=0xC9
Define.REGISTER_MIN_H_RED=0xCA
Define.REGISTER_MAX_H_RED=0xCC
Define.REGISTER_MIN_H_GREEN=0xCE
Define.REGISTER_MAX_H_GREEN=0xD0
Define.REGISTER_MIN_H_BLUE=0xD2
Define.REGISTER_MAX_H_BLUE=0xD4
Define.REGISTER_MIN_H_YELLOW=0xD6
Define.REGISTER_MAX_H_YELLOW=0xD8

Define.MODE_COLOR=0x00
Define.MODE_LIGHT=0x01
Define.MODE_LIGHT2=0x02 ##prende el led


class colorbk(object):
    ##variables estaticas aqui
    colorcases = {
        "1":"white",
        "2":"black",
        "3":"red",
        "4":"green",
        "5":"blue",
        "6":"yellow",
        "error":"error"
        }
    
    def __init__(self,portnum=0):
        self.portnum = portnum
        self.modestate = Define.MODE_LIGHT
        
    ##regresa el color detectado
    ##white 1,black 2,red 3,green 4,blue 5,yellow 6
    ##o la raw data del color seleccionado(0-255)
    def read(self,*argsx):
        if(len(argsx)!=0): ##para checar si esta vacio o no
            colorselect = argsx[0]
            if(colorselect=="white"):
                colorret="error"
                error_com = wirebk.Port_Enabled(self.portnum);
                if(error_com==0):
                    if(self.modestate!=Define.MODE_LIGHT):
                        wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_MODE,Define.MODE_LIGHT)
                        self.modestate = Define.MODE_LIGHT
                        time.sleep(0.02)
                    wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_ADDR_POINTER,Define.REGISTER_AMBIENT)    
                    colorret = wirebk.ReadBk(Define.SLAVE_ADDRESS_COLORSENSOR,1)[0]
                    if(colorret=="error"):
                        print("color sensor {} not working".format(self.portnum))
                else:
                    print("comunication i2c not working")
                wirebk.Port_Enabled(0)
                return(colorret)
            elif(colorselect=="white2"):
                colorret="error"
                error_com = wirebk.Port_Enabled(self.portnum);
                if(error_com==0):
                    if(self.modestate!=Define.MODE_LIGHT2):
                        wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_MODE,Define.MODE_LIGHT2)
                        self.modestate = Define.MODE_LIGHT2
                        time.sleep(0.02)
                    wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_ADDR_POINTER,Define.REGISTER_AMBIENT)    
                    colorret = wirebk.ReadBk(Define.SLAVE_ADDRESS_COLORSENSOR,1)[0]
                    if(colorret=="error"):
                        print("color sensor {} not working".format(self.portnum))
                else:
                    print("comunication i2c not working")
                wirebk.Port_Enabled(0)
                return(colorret)
            else:
                colorret="error"
                error_com = wirebk.Port_Enabled(self.portnum);
                if(error_com==0):
                    if(self.modestate!=Define.MODE_COLOR):
                        wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_MODE,Define.MODE_COLOR)
                        self.modestate = Define.MODE_COLOR
                        time.sleep(0.02)
                    if(colorselect=="red"):
                        wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_ADDR_POINTER,Define.REGISTER_SCALED_RED)    
                    elif(colorselect=="green"):
                        wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_ADDR_POINTER,Define.REGISTER_SCALED_GREEN)    
                    elif(colorselect=="blue"):
                        wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_ADDR_POINTER,Define.REGISTER_SCALED_BLUE)    
                    colorret = wirebk.ReadBk(Define.SLAVE_ADDRESS_COLORSENSOR,1)[0]
                    if(colorret=="error"):
                        print("color sensor {} not working".format(self.portnum))
                else:
                    print("comunication i2c not working")
                wirebk.Port_Enabled(0)
                return(colorret)
        else:
            colorret="error"
            error_com = wirebk.Port_Enabled(self.portnum);
            if(error_com==0):
                if(self.modestate!=Define.MODE_COLOR):
                    wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_MODE,Define.MODE_COLOR)
                    self.modestate = Define.MODE_COLOR
                    time.sleep(0.02)
                wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_ADDR_POINTER,Define.REGISTER_COLOR)    
                colorret = wirebk.ReadBk(Define.SLAVE_ADDRESS_COLORSENSOR,1)[0]
                if(str(colorret) in self.colorcases):
                    colorret = self.colorcases[str(colorret)]
                    if(colorret=="error"):
                        print("color sensor {} not working".format(self.portnum))
                else:
                    colorret="error"
                    print("color sensor {} not working".format(self.portnum)) 
            else:
                print("comunication i2c not working")
            wirebk.Port_Enabled(0)
            return(colorret)

        
    ##para calibrar el sensor
    def set(self,colorselect):
        colorret="error"
        error_com = wirebk.Port_Enabled(self.portnum);
        if(error_com==0):
            if(self.modestate!=Define.MODE_COLOR):
                wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_MODE,Define.MODE_COLOR)
                self.modestate = Define.MODE_COLOR
                time.sleep(0.02)
            if(colorselect=="white"):
                wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_START_CAL,1)    
            elif(colorselect=="black"):
                wirebk.WriteBk(Define.SLAVE_ADDRESS_COLORSENSOR,Define.REGISTER_START_CAL,2)    
        else:
            print("comunication i2c not working")
        wirebk.Port_Enabled(0)
    

        
