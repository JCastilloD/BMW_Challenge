#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 22:00:00 2018

@author: Rene
"""
import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor
import time

perimeter=18.85
db_p=25
vel=150
n=0
#Declaration of the motors
motorI = motor.motorbk(7)
motorD = motor.motorbk(6)

Route=[[1, 1], [2, 1], [3, 1], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4], [5, 5], (6.0,5.0), [7, 5], [7,6], [6, 6], [6, 7], [5, 7], [4, 7], [3, 7], (2.0, 7.0), [1, 7], [1, 6], [2, 6], [3, 6], [4, 6], (4.0, 5.0), [4, 4], [4, 3], [5,3], [5, 2], (6.0, 2.0), [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]

act_state=[(0,0)]
nxt_state=[(0,0)]
calc_state=[(0,0)]
n_points=len(Route)-1
bx=1
by=1
ori_car=0
#count=0

def avanza_odom(v,dist): #Move forward n centimeters
    turns=dist/perimeter
    motorI.turn(-v,turns)
    motorD.turn(v,turns)
    motorI.wait()
    motorD.wait()
    
def gira_d_odom(v): #Rotate 90 degrees cw
    #Secuence of rotation with compensation x and y
    motorI.move(-v,70)
    motorD.move(v,70)
    motorI.wait()
    motorD.wait()
    #time.sleep(5)
    motorI.move(-v,240)#232
    motorD.move(-v,240)#232
    motorI.wait()
    motorD.wait()
    #time.sleep(5)
    motorI.move(-v,85)#76
    motorD.move(v,85)#76
    motorI.wait()
    motorD.wait()
    #time.sleep(2)
    
def gira_i_odom(v): #Rotate 90 degrees ccw
    #Secuence of rotation with compensation x and y
    motorI.move(v,70)
    motorD.move(-v,70)
    motorI.wait()
    motorD.wait()
    #time.sleep(5)
    motorI.move(v,240)#232
    motorD.move(v,240)#232
    motorI.wait()
    motorD.wait()
    #time.sleep(5)
    motorI.move(v,85)#76
    motorD.move(-v,85)#76
    motorI.wait()
    motorD.wait()
    #time.sleep(2)

while(n<n_points): #While the route has not been completed
    if(n==0):
        ori_car=1
    flag=False
    act_state=Route[n]
    nxt_state=Route[n+1]
    calc_state=[(nxt_state[0]-act_state[0]),(nxt_state[1]-act_state[1])]
    
    if(calc_state[0]==1 and calc_state[1]==0):#Move along axis x
        if(ori_car==1 and flag==False):
            avanza_odom(vel,db_p)
            #print(count,'Avanza')
            #count+=1
            ori_car=1
            flag=True
        elif(ori_car==3 and flag==False):
            gira_d_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira derecha y avanza')
            #count+=1
            ori_car=1
            flag=True
        elif(ori_car==4 and flag==False):
            gira_i_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira izquierda y avanza')
            #count+=1
            ori_car=1
            flag=True
        n+=1

    elif(calc_state[0]==-1 and calc_state[1]==0):#Move along axis -x
        if(ori_car==2 and flag==False):
            avanza_odom(vel,db_p)
            #print(count,'Avanza')
            #count+=1
            ori_car=2
            flag=True
        elif(ori_car==3 and flag==False):
            gira_i_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira izquierda y avanza')
            #count+=1
            ori_car=2
            flag=True
        elif(ori_car==4 and flag==False):
            gira_d_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira derecha y avanza')
            #count+=1
            ori_car=2
            flag=True
        n+=1

    elif(calc_state[0]==0 and calc_state[1]==1):#Move along axis y
        if(ori_car==1 and flag==False):
            gira_i_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira izquierda y avanza')
            #count+=1
            ori_car=3
            flag=True
        elif(ori_car==2 and flag==False):
            gira_d_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira derecha y avanza')
            #count+=1
            ori_car=3
            flag=True
        elif(ori_car==3 and flag==False):
            avanza_odom(vel,db_p)
            #print(count,'Avanza')
            #count+=1
            ori_car=3
            flag=True
        n+=1

    elif(calc_state[0]==0 and calc_state[1]==-1):#Move along axis -y
        if(ori_car==1 and flag==False):
            gira_d_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira derecha y avanza')
            #count+=1
            ori_car=4
            flag=True
        elif(ori_car==2 and flag==False):
            gira_i_odom(vel)
            avanza_odom(vel,db_p)
            #print(count,'Gira izquierda y avanza')
            #count+=1
            ori_car=4
            flag=True
        elif(ori_car==4 and flag==False):
            avanza_odom(vel,db_p)
            #print(count,'Avanza')
            #count+=1
            ori_car=4
            flag=True
        n+=1
    else:
    #Apaga los motores
    motorI.set(0)
    motorD.set(0) 
        #print('Deten los motores')
        n+=1
    
print('Se completaron todos los puntos')
ori_car=0
    
#Apaga los motores
motorI.set(0)
motorD.set(0)    
