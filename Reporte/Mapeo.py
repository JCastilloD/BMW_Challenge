import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor
import colorbk as colorx
import distancebk as distance
import numpy as np
import time

# SENS!!!!!!!
def Sopas():
    sensor = colorx.colorbk(1)
    sensor2 = colorx.colorbk(2)
    print("start")
    time.sleep(1)
    sensor.set("black")
    sensor2.set("black")
    print("Ponte verga")
    time.sleep(4)
    sensor.set("white")
    sensor2.set("white")
    a=input()
    print("¡INICIA!")
# SENS!!!!!!!


motorI = motor.motorbk(7)
motorD = motor.motorbk(6)
encoD = motorD.readkappa()
encoD = encoD
encoDD = encoD
GG = 690
GG2 = 750
GG3 = 460
i=0
tt=0
u=0
# 792 encoder

matrix = np.zeros((9,9))

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

x1a = 0
y1a = 0
x2a = 0
y2a = 0
x3a = 0
y3a = 0
x4a = 0
y4a = 0

x1b = 0
y1b = 0
x2b = 0
y2b = 0
x3b = 0
y3b = 0
x4b = 0
y4b = 0

cajas = 0
def colores():
    global SI, SD,x1,x2,x3,x4,y1,y2,y3,y4,x,y
    SI=sensorI.read()
    SD=sensorD.read()
    if (SD==SI):
        if(SD=="red"):
            cajas+=1
            return (11)
        else:
            if(SD=="green"):
                cajas+=1
                return (22)
            else:
                if(SD=="yellow"):
                    cajas+=1
                    return (44)
                else:
                    if(SD=="blue"):
                        cajas+=1
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
pos=0




ultra = distance.distancebk(3)

cruce = 0
umbralDiff = 15 #Umbral que detecta si los sensores ven cosas sitintas. Falta hacerlo dinamico
umbralLight = 65 #Umbral que detecta si es blanco o negro. Falta hacerlo dinamico

#time.sleep(1)
td=0
ti=0
ED=0
#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
def corre1():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3,tt,td,ti,ED,pos,x1a,x2a,x3a,x4a,y1a,y2a,y3a,y4a,x1b,x2b,x3b,x4b,y1b,y2b,y3b,y4b
    motorI.set(0)
    motorD.set(0)
    u=ultra.read()
    motorI.set(ti)
    motorD.set(td)
    while((ultra.read()>8) and (y < 7)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                ti=-255
                td=200
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = motorD.readkappa()
            ED = encoD-encoDD
            if (ED>=GG):
                
                encoDD = encoD+(ED-GG)*0 # SERA
                print("Enco D: ",ED-GG)
                cruce+=1
                y+=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
                motorI.set(0)# COSA
                motorD.set(0)
                i=colores()
                if(i):
                    matrix[x][y]=i
                    matrix[x][y+1]=i/11
                    matrix[x][y-1]=i/11
                    if(i==11):
                        x1a=x
                        x1b=x
                        y1a=y+1
                        y1b=y-1
                    else:
                        if(i==22):
                            x2a=x
                            x2b=x
                            y2a=y+1
                            y2b=y-1
                        else:
                            if(i==33):
                                x3a=x
                                x3b=x
                                y3a=y+1
                                y3b=y-1
                            else:
                                x4a=x
                                x4b=x
                                y4a=y+1
                                y4b=y-1
                        
                
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
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

    encoD = abs(motorD.readkappa())
    
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
                ti=-255
                td=200
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = abs(motorD.readkappa())
            ED = encoD-encoDD
            if (ED>=GG2):
                
                encoDD = encoD+(ED-GG)*0 #SERA
                print("Enco D: ",ED-GG)
                cruce-=1
                y-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
    giro(1)
    

    if(x<7):
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        x+=1
        i=colores()
        if(i):
            matrix[x][y]=i
            matrix[x+1][y]=i/11
            matrix[x-1][y]=i/11
            motorI.move(-velg,GG3)
            motorD.move(velg,GG3)
            motorI.wait()
            motorD.wait()
            if(i==11):
                x1a=x-1
                x1b=x+1
                y1a=y
                y1b=y
            else:
                if(i==22):
                    x2a=x-1
                    x2b=x+1
                    y2a=y
                    y2b=y
                else:
                    if(i==33):
                        x3a=x-1
                        x3b=x+1
                        y3a=y
                        y3b=y
                    else:
                        x4a=x-1
                        x4b=x+1
                        y4a=y
                        y4b=y
            x+=1
        giro(1)
        
    else:
        giro(1)
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        y+=1
        giro(1)

    encoD = motorD.readkappa()
    encoDD = encoD

    print(matrix)

#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
def corre2():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3,tt,td,ti,ED,pos,x1a,x2a,x3a,x4a,y1a,y2a,y3a,y4a,x1b,x2b,x3b,x4b,y1b,y2b,y3b,y4b
    motorI.set(0)
    motorD.set(0)
    u=ultra.read()
    motorI.set(ti)
    motorD.set(td)
    while((ultra.read()>8) and (x > 1)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                ti=-255
                td=200
                #print("Derecha")
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = motorD.readkappa()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)*0
                cruce+=1
                x-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
                motorI.set(0)# COSA
                motorD.set(0)
                i=colores()
                if(i):
                    matrix[x][y]=i
                    matrix[x-1][y]=i/11
                    matrix[x+1][y]=i/11
                    if(i==11):
                        x1a=x-1
                        x1b=x+1
                        y1a=y
                        y1b=y
                    else:
                        if(i==22):
                            x2a=x-1
                            x2b=x+1
                            y2a=y
                            y2b=y
                        else:
                            if(i==33):
                                x3a=x-1
                                x3b=x+1
                                y3a=y
                                y3b=y
                            else:
                                x4a=x-1
                                x4b=x+1
                                y4a=y
                                y4b=y
                    
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
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

    encoD = abs(motorD.readkappa())
    
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
                ti=-255
                td=200
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = abs(motorD.readkappa())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)*0
                cruce-=1
                x+=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
    giro(1)
    

    if(y<7):
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        y+=1
        i=colores()
        if(i):
            matrix[x][y]=i
            matrix[x1][y+1]=i/11
            matrix[x1][y-1]=i/11
            motorI.move(-velg,GG3)
            motorD.move(velg,GG3)
            motorI.wait()
            motorD.wait()
            if(i==11):
                x1a=x
                x1b=x
                y1a=y+1
                y1b=y-1
            else:
                if(i==22):
                    x2a=x
                    x2b=x
                    y2a=y+1
                    y2b=y-1
                else:
                    if(i==33):
                        x3a=x
                        x3b=x
                        y3a=y+1
                        y3b=y-1
                    else:
                        x4a=x
                        x4b=x
                        y4a=y+1
                        y4b=y-1
            y+=1
        giro(1)
        
    else:
        giro(1)
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        x-=1
        giro(1)

    encoD = motorD.readkappa()
    encoDD = encoD
    print(matrix)
        
#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
def corre3():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3,tt,td,ti,ED,pos,x1a,x2a,x3a,x4a,y1a,y2a,y3a,y4a,x1b,x2b,x3b,x4b,y1b,y2b,y3b,y4b
    motorI.set(0)
    motorD.set(0)
    u=ultra.read()
    motorI.set(ti)
    motorD.set(td)
    while((ultra.read()>8) and (y > 1)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                #print("Derecha")
                ti=-255
                td=200
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = motorD.readkappa()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)*0
                cruce+=1
                y-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
                i=colores()
                if(i):
                    matrix[x][y]=i
                    matrix[x][y+1]=i/11
                    matrix[x][y-1]=i/11
                    if(i==11):
                        x1a=x
                        x1b=x
                        y1a=y+1
                        y1b=y-1
                    else:
                        if(i==22):
                            x2a=x
                            x2b=x
                            y2a=y+1
                            y2b=y-1
                        else:
                            if(i==33):
                                x3a=x
                                x3b=x
                                y3a=y+1
                                y3b=y-1
                            else:
                                x4a=x
                                x4b=x
                                y4a=y+1
                                y4b=y-1
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
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

    encoD = abs(motorD.readkappa())
    
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
                ti=-255
                td=200
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = abs(motorD.readkappa())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)*0
                cruce-=1
                y-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
    giro(1) 

    if(x>1):
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        x-=1
        i=colores()
        if(i):
            matrix[x][y]=i
            matrix[x+1][y]=i/11
            matrix[x-1][y]=i/11
            motorI.move(-velg,GG3)
            motorD.move(velg,GG3)
            motorI.wait()
            motorD.wait()
            if(i==11):
                x1a=x-1
                x1b=x+1
                y1a=y
                y1b=y
            else:
                if(i==22):
                    x2a=x-1
                    x2b=x+1
                    y2a=y
                    y2b=y
                else:
                    if(i==33):
                        x3a=x-1
                        x3b=x+1
                        y3a=y
                        y3b=y
                    else:
                        x4a=x-1
                        x4b=x+1
                        y4a=y
                        y4b=y
            x-=1
        giro(1)
        
    else:
        giro(1)
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        y-=1
        giro(1)

    encoD = motorD.readkappa()
    encoDD = encoD

    print(matrix)

#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
def corre4():
    global x,y,SI,SD,vel,encoD,ED,GG,cruce,umbralDiff,matrix,encoDD,velg,GG2,GG3,tt,td,ti,ED,pos,x1a,x2a,x3a,x4a,y1a,y2a,y3a,y4a,x1b,x2b,x3b,x4b,y1b,y2b,y3b,y4b
    motorI.set(0)
    motorD.set(0)
    u=ultra.read()
    motorI.set(ti)
    motorD.set(td)
    while((ultra.read()>8) and (x < 7)):
        SI = sensorI.read("white2")
        SD = sensorD.read("white2")
        #print(SI, SD)
        if((abs(SI-SD))>umbralDiff): #
            if((SI-SD)>0):
                motorI.set(-vel)
                motorD.set(200)
                #print("Derecha")
                ti=-255
                td=200
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")l
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = motorD.readkappa()
            ED = encoD-encoDD
            if (ED>=GG):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)*0
                cruce+=1
                x+=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
                i=colores()
                if(i):
                    matrix[x][y]=i
                    matrix[x+1][y]=i/11
                    matrix[x-1][y]=i/11
                    
                    if(i==11):
                        x1a=x-1
                        x1b=x+1
                        y1a=y
                        y1b=y
                    else:
                        if(i==22):
                            x2a=x-1
                            x2b=x+1
                            y2a=y
                            y2b=y
                        else:
                            if(i==33):
                                x3a=x-1
                                x3b=x+1
                                y3a=y
                                y3b=y
                            else:
                                x4a=x-1
                                x4b=x+1
                                y4a=y
                                y4b=y
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
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

    encoD = abs(motorD.readkappa())
    
    encoDD = encoD
    

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
                ti=-255
                td=200
            else: 
                motorI.set(-200)
                motorD.set(255)
                #print("Izquierda")
                ti=-200
                td=255
        else:
            motorI.set(0)
            motorD.set(0)
            encoD = abs(motorD.readkappa())
            ED = encoD-encoDD
            if (ED>=GG2):
                print("Enco D: ",ED)
                encoDD = encoD+(ED-GG)*0
                cruce-=1
                x-=1
                if(matrix[x][y]==0):
                    matrix[x][y]=-1
                #paro(tt)
            motorI.set(-255)
            motorD.set(255)
            ti=-255
            td=255
    giro(1)    

    if(y>1):
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        giro(1)
        y-=1
    else:
        giro(1)
        motorI.move(-velg,GG3)
        motorD.move(velg,GG3)
        motorI.wait()
        motorD.wait()
        y-=1
        i=colores()
        if(i):
            matrix[x][y]=i
            matrix[x][y+1]=i/11
            matrix[x][y-1]=i/11
            motorI.move(-velg,GG3)
            motorD.move(velg,GG3)
            motorI.wait()
            motorD.wait()
            if(i==11):
                x1a=x
                x1b=x
                y1a=y+1
                y1b=y-1
            else:
                if(i==22):
                    x2a=x
                    x2b=x
                    y2a=y+1
                    y2b=y-1
                else:
                    if(i==33):
                        x3a=x
                        x3b=x
                        y3a=y+1
                        y3b=y-1
                    else:
                        x4a=x
                        x4b=x
                        y4a=y+1
                        y4b=y-1
            x+=1
        giro(1)
        

    encoD = motorD.readkappa()
    encoDD = encoD

    print(matrix)
        
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
Sopas()
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
#3

pos=[(np.array((x1a,y1a)))]
pos=[(np.array((x1b,y1b)))]
pos=[(np.array((x2a,y2a)))]
pos=[(np.array((x2b,y2b)))]
pos=[(np.array((x3a,y3a)))]
pos=[(np.array((x3b,y3b)))]
pos=[(np.array((x4a,y4a)))]
pos=[(np.array((x4b,y4b)))]

