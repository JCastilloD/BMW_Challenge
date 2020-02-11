import sys
import atexit
sys.path.append("/home/pi/bmw/libs")

import time
import cv2
import numpy as np

import distancebk as distance
import motorbk as motor
import colorbk as colorx
import boardIObk as board
import powerbk as power
import IMUbk as IMU

###funcion para terminar el programa
def exit_handler():
    motorL.set(0)
    motorR.set(0)
    board1.CleanUp()
    print ('End')

##registra funcion que se llama antes de terminar todo
atexit.register(exit_handler)

###funcion para la interrupcion
def End_All_Callable():
    sys.exit("interrupt")

####configuracion de botones y leds
board1 = board.boardbk()
board1.Enable_Interrupt_Button(1,End_All_Callable)
board1.Enable_Button(2)
board1.Enable_Led(1)
board1.Set_Led(1,0)
board1.Enable_Led(2)
board1.Set_Led(2,0)
board1.Enable_Led(3)
board1.Set_Led(3,0)

#########inicializamos los objetos de los sensores#################
sensorD = distance.distancebk(3)  ##distance sensor
motorL = motor.motorbk(7) ##Left motor
motorR = motor.motorbk(6) ##Right motor
sensorCL = colorx.colorbk(1) ##Color sensor left
sensorCR = colorx.colorbk(2) ##Color sensor right
powerS = power.powerbk() ##sensor de voltaje y corriente
imu = IMU.IMUbk()  ##objeto imu


#####loop infinito
try:
    while(1):
        print("sensor distancia: {} cm".format(sensorD.read()))
        time.sleep(0.01) ##para no saturar
        
except (KeyboardInterrupt, SystemExit):
    pass





