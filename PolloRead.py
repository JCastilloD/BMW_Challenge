import sys
import time
sys.path.append("/home/pi/bmw/libs")
import colorbk as colorx

sensor = colorx.colorbk(1)
sensor2 = colorx.colorbk(2)

tri=20
tbi=30
tgi=30
trd=20
tbd=30
tgd=30



print("Izquierda: ")
ri=sensor.read("red")
print(ri)
#time.sleep(1)
gi=sensor.read("green")
print(gi)
#time.sleep(1)
bi=sensor.read("blue")
print(bi)
#time.sleep(1)

if(tri<ri and tgi<gi and tbi<bi):
    if(100<ri and 100<gi and 100<bi):
        print("Techo")
    else:
        print("Amarillo no me pongo, Amarillo es mi color")
elif(tri<ri and tgi>gi and tbi>bi):
    print("Rojos Labios Rojos")
elif(tri>ri and tgi>gi and tbi>bi):
    if(1>ri and 1>gi and 1>bi):
        print("Blackie")
    else:
        print("ALVerde")
else:
    print("No Sabo... ")
    print(tri<ri)
    print(tgi<gi)
    print(tbi<bi)



print("Derecha: ")
rd=sensor.read("red")
print(rd)
#time.sleep(1)
gd=sensor.read("green")
print(gd)
#time.sleep(1)
bd=sensor.read("blue")
print(bd)
#time.sleep(1)

if(tri<ri and tgi<gi and tbi<bi):
    if(100<ri and 100<gi and 100<bi):
        print("Techo")
    else:
        print("Amarillo no me pongo, Amarillo es mi color")
elif(trd<rd and tgd>gd and tbd>bd):
    print("Rojos Labios Rojos")
elif(trd>rd and tgd>gd and tbd>bd):
    if(1>rd and 1>gd and 1>bd):
        print("Blackie")
    else:
        print("ALVerde")
else:
    print("No Sabo... ")
    print(trd<rd)
    print(tgd<gd)
    print(tbd<bd)
