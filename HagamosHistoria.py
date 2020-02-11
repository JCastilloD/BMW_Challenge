import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor
import colorbk as colorx
import distancebk as distance
import numpy as np
import time

motorI = motor.motorbk(7)
motorD = motor.motorbk(6)
encoD = motorD.read()
encoD = encoD
encoDD = encoD
GG = 640
GG2 = 710
GG3 = 720
i=0

# 792 encoder

matrix = np.zeros((8,8))

vel=255
velg=vel # Solo se usara si es necesario

#*************************

def paro(tuna):
    motorI.set(0)# COSA
    motorD.set(0)
    time.sleep(tuna)
    motorI.set(-255)
    motorD.set(255)# COSA
    
SI = 0
SD = 0

def colores():
    global SI, SD
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
                        return (0)

def giro(cuadrante):
    if cuadrante==1:
        motor1 = motor.motorbk(7)
        motor2 = motor.motorbk(6)
        motor1.move(-velg,70)
        motor2.move(velg,70)
        motor1.wait()
        motor2.wait()
        #time.sleep(5)
        motor1.move(velg,240)#232
        motor2.move(velg,240)#232
        motor1.wait()
        motor2.wait()
        #time.sleep(5)
        motor1.move(velg,85)#76
        motor2.move(-velg,85)#76
        motor1.wait()
        motor2.wait()
        #time.sleep(2)

def giro2(cuadrante):
    if cuadrante==1:
        motor1 = motor.motorbk(7)
        motor2 = motor.motorbk(6)
        motor1.move(-velg,70)
        motor2.move(velg,70)
        motor1.wait()
        motor2.wait()
        #time.sleep(5)
        motor1.move(velg,-240)#232
        motor2.move(velg,-240)#232
        motor1.wait()
        motor2.wait()
        #time.sleep(5)
        motor1.move(velg,85)#76
        motor2.move(-velg,85)#76
        motor1.wait()
        motor2.wait()
        #time.sleep(2)

#motorI.set(-255)
#motorD.set(255)

sensorI = colorx.colorbk(1)
sensorD = colorx.colorbk(2)
b=0
x=1
y=1
pos=(x,y)


ultra = distance.distancebk(3)

cruce = 0
umbralDiff = 15 #Umbral que detecta si los sensores ven cosas sitintas. Falta hacerlo dinamico
umbralLight = 65 #Umbral que detecta si es blanco o negro. Falta hacerlo dinamico

#time.sleep(1)


#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
def corre1():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3
    while((ultra.read()>8) and (y < 7)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
        else:
            encoD = motorD.read()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce+=1
                y+=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                paro(1)
                motorI.set(0)# COSA
                motorD.set(0)
                i=colores()
                if(i):
                    matrix[x][y]=i
                    matrix[x-1][y+1]=i/11
                    matrix[x+1][y+1]=i/11
                
            motorI.set(-255)
            motorD.set(255)
            #*******************************
    motorI.set(0)
    motorD.set(0)
    if(y<7):
        if(ED>(GG*0.8)):
            y+=1
        matrix[x][y+1]=55
        matrix[x-1][y+1]=5
        matrix[x+1][y+1]=5

    
    #break
    print(cruce)


    giro(1)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    encoII = encoI

    #111
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
            encoD = abs(motorD.read())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce-=1
                y-=1
                matrix[x][y]=-1
                paro(1)
            motorI.set(-255)
            motorD.set(255)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    

    if(x<7):
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        giro2(1)
        x+=1
    else:
        giro2(1)
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        y+=1
        giro2(1)

    print(matrix)

#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
def corre2():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3
    while((ultra.read()>8) and (x > 1)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
        else:
            encoD = motorD.read()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce+=1
                x-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                paro(1)
                motorI.set(0)# COSA
                motorD.set(0)
                i=colores()
                if(i):
                    matrix[x-1][y]=i
                    matrix[x-1][y+1]=i/11
                    matrix[x-1][y-1]=i/11
            motorI.set(-255)
            motorD.set(255)
            #*******************************
    motorI.set(0)
    motorD.set(0)
    if(x>1):
        if(ED>(GG*0.8)):
            x-=1
        matrix[x-1][y]=55
        matrix[x-1][y+1]=5
        matrix[x-1][y-1]=5

    
    #break
    print(cruce)


    giro(1)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    

    #111
    while(x < 7):
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
            encoD = abs(motorD.read())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce-=1
                x+=1
                matrix[x][y]=-1
                paro(1)
            motorI.set(-255)
            motorD.set(255)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    encoII = encoI

    if(y<7):
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        giro2(1)
        y+=1
    else:
        giro2(1)
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        x-=1

    print(matrix)
        
#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
def corre3():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3
    while((ultra.read()>8) and (y > 1)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
        else:
            encoD = motorD.read()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce+=1
                y-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                paro(1)
                i=colores()
                if(i):
                    matrix[x][y-1]=i
                    matrix[x-1][y-1]=i/11
                    matrix[x+1][y-1]=i/11
            motorI.set(-255)
            motorD.set(255)
            #*******************************
    motorI.set(0)
    motorD.set(0)
    if(y>1):
        if(ED>(GG*0.8)):
            y-=1
        matrix[x][y-1]=55
        matrix[x-1][y-1]=5
        matrix[x+1][y-1]=5

    
    #break
    print(cruce)


    giro(1)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    

    #111
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
            encoD = abs(motorD.read())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce-=1
                y-=1
                matrix[x][y]=-1
                paro(1)
            motorI.set(-255)
            motorD.set(255)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    encoII = encoI

    if(x>1):
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        giro2(1)
        x-=1
    else:
        giro2(1)
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        y-=1

    print(matrix)

#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
def corre4():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3
    while((ultra.read()>8) and (x < 7)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
        else:
            encoD = motorD.read()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce+=1
                x+=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                paro(1)
                i=colores()
                if(i):
                    matrix[x+1][y]=i
                    matrix[x+1][y+1]=i/11
                    matrix[x+1][y-1]=i/11
            motorI.set(-255)
            motorD.set(255)
            #*******************************
    motorI.set(0)
    motorD.set(0)
    if(x<7):
        if(ED>(GG*0.8)):
            x+=1
        matrix[x+1][y]=55
        matrix[x+1][y+1]=5
        matrix[x+1][y-1]=5

    
    #break
    print(cruce)


    giro(1)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    encoII = encoI

    #111
    while(x > 1):
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
            encoD = abs(motorD.read())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)
                cruce-=1
                x-=1
                matrix[x][y]=-1
                paro(1)
            motorI.set(-255)
            motorD.set(255)
    giro(1)

    encoD = abs(motorD.read())
    encoI = abs(motorI.read())
    encoDD = encoD
    

    if(y>1):
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        giro2(1)
        y-=1
    else:
        giro2(1)
        motor1.move(-velg,GG3)
        motor2.move(velg,GG3)
        motor1.wait()
        motor2.wait()
        x+=1

    print(matrix)
        
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
t=0
while(t<7):
    corre1()
    t+=1
t=0
while(t<7):
    corre2()
    t+=1
t=0
while(t<7):
    corre3()
    t+=1
t=0
while(t<7):
    corre4()
    t+=1

motorI.set(0)
motorD.set(0)



