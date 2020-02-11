import sys
import time
sys.path.append("/home/pi/bmw/libs")
import colorbk as colorx

def pollosense(s):
    tri=20
    tbi=20
    tgi=20
    sensor = colorx.colorbk(s)
    ri=sensor.read("red")
    gi=sensor.read("green")
    bi=sensor.read("blue") 
    
    if(tri<ri and tgi<gi and tbi<bi):
        if(100<ri and 100<gi and 100<bi):
            print("Techo")
            return 5
        else:
            print("Amarillo no me pongo, Amarillo es mi color")
            return 2
    elif(tri<ri and tgi>gi and tbi>bi):
        print("Rojos Labios Rojos")
        return 1
    elif(tri>ri and tgi<gi and tbi>bi):
        print("ALVerde")
        return 2
    elif(tri>ri and tgi>gi and tbi>bi):
        if(1>ri and 1>gi and 1>bi):
            print("Blackie")
            return 0
        else:
            print("ALVerde")
            return 2
    else:
        print("No Sabo... ")
        print(tri<ri)
        print(tgi<gi)
        print(tbi<bi)
        return -1
