import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor
import colorbk as colorx
import distancebk as distance
import numpy as np
import time

matrix = np.zeros(8,8)
t=0

def colores():
    SI=sensorI.read()
    SD=sensorD.read()
    if (SD==SI):
        if(SD=="red"):
            return (11)
        else:
            if(SD=="green"):
                return (22)
            else:
                if(SD=="yellow"):
                    return (44)
                else:
                    if(SD=="blue"):
                        return (33)
                    else:
                        return 0

def giro(cuadrante):
    if cuadrante==1:
        motor1 = motor.motorbk(7)
        motor2 = motor.motorbk(6)
        motor1.move(-255,70)
        motor2.move(255,70)
        motor1.wait()
        motor2.wait()
        #time.sleep(5)
        motor1.move(255,232)
        motor2.move(255,232)
        motor1.wait()
        motor2.wait()
        #time.sleep(5)
        motor1.move(255,76)
        motor2.move(-255,76)
        motor1.wait()
        motor2.wait()
        #time.sleep(2)

motorI = motor.motorbk(7)
motorD = motor.motorbk(6)
motorI.set(-255)
motorD.set(255)

sensorI = colorx.colorbk(1)
sensorD = colorx.colorbk(2)
SI = 0
SD = 0
b=0
x=1
y=1
pos=(x,y)


ultra = distance.distancebk(3)

cruce = 0
umbralDiff = 20 #Umbral que detecta si los sensores ven cosas sitintas. Falta hacerlo dinamico
umbralLight = 70 #Umbral que detecta si es blanco o negro. Falta hacerlo dinamico

#time.sleep(1)

while((ultra.read()>7) and (y < 7)):
    SI = sensorI.read("white2")
    SD = sensorD.read("white2")
    #print(SI, SD)
    if((abs(SI-SD))>umbralDiff): #
        if((SI-SD)>0):
            motorI.set(-255)
            motorD.set(200)
            #print("Derecha")
        else: 
            motorI.set(-200)
            motorD.set(255)
            #print("Izquierda")
    else:
        t+=1
        if(SI>umbralLight and SD>umbralLight): #
            motorI.set(-255)
            motorD.set(255)
            #print("Centro")
            if(b):
                print("Negro ",t)
                t=0
                b=0
        else:
            motorI.set(-255)
            motorD.set(255) # Checar caso Azul
            if (b==0):
                print("Cruce")
                print(SI, SD)
                cruce+=1
                y=+1
                b=1
                print("Blanco ",t)
                t=0
                matrix[x][y]=-1
if(y<7):
    matrix[x][y+1]=5
                
#break
print(cruce)
print (matrix)

giro(1)
giro(1)

motorI.set(-255)
motorD.set(255)

while(y > 1):
    SI = sensorI.read("white2")
    SD = sensorD.read("white2")
    #print(SI, SD)
    if((abs(SI-SD))>umbralDiff): #
        if((SI-SD)>0):
            motorI.set(-255)
            motorD.set(200)
            #print("Derecha")
        else: 
            motorI.set(-200)
            motorD.set(255)
            #print("Izquierda")
    else:   
        if(SI>umbralLight and SD>umbralLight): #
            motorI.set(-255)
            motorD.set(255)
            #print("Centro")
            if(b):
                b=0
        else:
            motorI.set(-255)
            motorD.set(255) # Checar caso Azul
            if (b==0):
                print("Cruce")
                print(SI, SD)
                y=-1
                b=1
                matrix[x][y]=-1
giro(1)

motorI.set(0)
motorD.set(0)
