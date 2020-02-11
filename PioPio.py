import sys
import time
import pollolib
sys.path.append("/home/pi/bmw/libs")
import colorbk as colorx


print("***** IZQUIERDO *****")
print(pollolib.pollosense(1))
print("***** DERECHO *****")
print(pollolib.pollosense(2))