import os
import time
###para incrementar el clock stretching de i2c
os.system('sudo libs/files/i2c1_set_clkt_tout 2000')
##para arreglar el bug de que se cambia la frecuencia del i2c derrepente
os.system('sudo sh -c "echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor"')
time.sleep(0.1)
import smbus
import const
Define = const._const()

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
Define.MULTIPLEXOR_ADDRESS=0x70 

def Port_Enabled(Port_Num):
    Port_Enable_Bits=0
    if(Port_Num==8):
        Port_Enable_Bits=0b11111111
    elif(Port_Num==7):
        Port_Enable_Bits=0b1
    elif(Port_Num==6):
        Port_Enable_Bits=0b10
    elif(Port_Num==5):
        Port_Enable_Bits=0b100
    elif(Port_Num==4):
        Port_Enable_Bits=0b1000
    elif(Port_Num==3):
        Port_Enable_Bits=0b100000
    elif(Port_Num==2):
        Port_Enable_Bits=0b1000000
    elif(Port_Num==1):
        Port_Enable_Bits=0b10000000
    else:
        Port_Enable_Bits=0
    try:
        bus.write_byte(Define.MULTIPLEXOR_ADDRESS, Port_Enable_Bits)
        return(0)
    except Exception as e:
        #print(e)
        return("error")
    
##para mandar bytes o arreglo de bytes por i2c
def WriteBk(Addr_Dev,Reg_Dev,Data_Dev):
    ##checa si es un arreglo o no lo que se va mandar
    if(not(isinstance(Data_Dev, list))):
        try:
            bus.write_byte_data(Addr_Dev,Reg_Dev,Data_Dev)
            return(0)
        except Exception as e:
            #print(e)
            return("error")
    else:
        try:
            bus.write_i2c_block_data(Addr_Dev,Reg_Dev,Data_Dev)
            return(0)
        except Exception as e:
            #print(e)
            return("error")

##para mandar 1 byte
def WriteBk1byte(Addr_Dev,Data_Dev):
    try:
        bus.write_byte(DAddr_Dev,Data_Dev)
        return(0)
    except Exception as e:
        #print(e)
        return("error")

##para leer 1 byte por i2c
def ReadBk(Addr_Dev,Bytes2Read):
    datareaded = ["error"]
    try:
        datareaded=bus.read_i2c_block_data(Addr_Dev,0,Bytes2Read)
        return(datareaded)
    except Exception as e:
        #print(e)
        return(datareaded)


##para leer 1 byte por i2c
def ReadBk2(Addr_Dev,Bytes2Read,address):
    datareaded = ["error"]
    try:
        datareaded=bus.read_i2c_block_data(Addr_Dev,address,Bytes2Read)
        return(datareaded)
    except Exception as e:
        #print(e)
        return(datareaded)




        
