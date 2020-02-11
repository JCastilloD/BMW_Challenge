import sys
sys.path.append("/home/pi/bmw/libs")
import motorbk as motor
import colorbk as colorx
import time

class Move(object):

	def __init__(self):
		self.motorLeft = motor.motorbk(7)
		self.motorRight = motor.motorbk(8)
		self.WheelPerimeter = 18.85
		self.RobotDiameter = 5.7
		self.RightWhSpeed = 255
		self.LeftWhSpeed = 255
		

	def DirecMove(self, direction):
		if direction == "fw":
			self.motorLeft.turn(self.LeftWhSpeed,1)
			self.motorRight.turn(-self.RightWhSpeed,1)
			self.motorLeft.wait()
			self.motorRight.wait()
		else if direction ==  "bw":
			self.motorLeft.turn(-self.LeftWhSpeed,1)
			self.motorRight.turn(self.RightWhSpeed,1)
			self.motorLeft.wait()
			self.motorRight.wait()
		else:
			print("No right command found, fw = forward   bw = backward")

	def Rotate(self, direction):
		if direction == "cw":
			self.motorLeft.turn(self.LeftWhSpeed,1)
			self.motorRight.turn(self.RightWhSpeed,1)
			self.motorLeft.wait()
			self.motorRight.wait()
		else if direction == "ccw":
			self.motorLeft.turn(-self.LeftWhSpeed,1)
			self.motorRight.turn(-self.RightWhSpeed,1)
			self.motorLeft.wait()
			self.motorRight.wait()
		else:
			print("No right command found, cw = clockwise   ccw = counter-clockwise")			


	def RotateDegr(self, direction, degrees):
		turns = Deg2Wheelturns(degrees)
		if direction == "cw":
			self.motorLeft.turn(self.LeftWhSpeed,turns)
			self.motorRight.turn(self.RightWhSpeed,turns)
			self.motorLeft.wait()
			self.motorRight.wait()
		else if direction == "ccw":
			self.motorLeft.turn(-self.LeftWhSpeed,turns)
			self.motorRight.turn(-self.RightWhSpeed,turns)
			self.motorLeft.wait()
			self.motorRight.wait() 

	def Deg2Wheelturns(degrees):
		turns = (degrees*(3.1415)*self.RobotDiameter)/(2*180*self.WheelPerimeter)
		return turns

	def MoveDistance(self, direction, distance):
		turns = distance/self.WheelPerimeter
		if direction == "fw":
			self.motorLeft.turn(self.LeftWhSpeed,turns)
			self.motorRight.turn(-self.RightWhSpeed,turns)
			self.motorLeft.wait()
			self.motorRight.wait()
		else if direction ==  "bw":
			self.motorLeft.turn(-self.LeftWhSpeed,turns)
			self.motorRight.turn(self.RightWhSpeed,turns)
			self.motorLeft.wait()
			self.motorRight.wait()

	def SetMotorSpeeds(self, RightSpeed, LeftSpeed):
		self.RightWhSpeed = RightSpeed
		self.LeftWhSpeed = LeftSpeed


MoveRobot = Move()
count=0

colorsValues = {"red" : 0, "green" : 0, "blue" : 0, "white": 0, "black" : 0}
MoveRobot.MoveDistance("fw",100)
while():
    for i in colorsValues:
        colorsValues[i]=sensor.read(i)
        #max(colorsValues[])
        #print(sensor.read("red"))


#keep = True

'''while keep:
	movement = input("Which move is gonna do the robot? 1 = rotate,   0 = translate   ")
	if movement == 1:
		direction = input("Rotation direction? 1 = clockWise,    0 = counter Clockwise   ")
		if direction == 1:
			degrees = input("How many degrees?  ")
			MoveRobot.Rotate("cw", degrees)
		else if direction == 0:
			degrees = input("How many degrees?  ")
			MoveRobot.Rotate("ccw", degrees)
		else:
			print("Not a right movement")
	else if movement == 0:
		direction = input("Rotation direction? 1 = forward,    0 = backwards   ")
		if direction == 1:
			distance = input("How many centimeters?  ")
			MoveRobot.MoveDistance("fw", distance)
		else if direction == 0:
			distance = input("How many centimeters?  ")
			MoveRobot.Rotate("bw", distance)
		else:
			print("Not a right movement")

	keep = input("Another movement?   1 = yes,    0 = no")
s motor'''

