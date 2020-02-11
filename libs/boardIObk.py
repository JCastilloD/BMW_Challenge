import RPi.GPIO as GPIO
import time
import const
Define = const._const()

GPIO.setmode(GPIO.BCM)  ##io's referenced to chip numbers

###defines of all io pins
Define.BUTTON_1=5
Define.BUTTON_2=6
Define.LED_1=13
Define.LED_2=19
Define.LED_3=26

###variable to save the real function run in interrupt of button 1
global Callfunction_Button1
Callfunction_Button1 = None

##function called in interrupt of button 1
def Callfunction_Interrupt_Button1(pin):
    global Callfunction_Button1
    countermark = 0
    while(GPIO.input(Define.BUTTON_1)==0): ##To avoid false clicks in the button
        countermark = countermark+1
        if(countermark>=100000):
            countermark=100000
    if(countermark>=100000):
        try:
            Callfunction_Button1()
        except TypeError:
            print("Error running interrupt function, check that function doesnt have arguments or errors")

###variable to save the real function run in interrupt of button 2
global Callfunction_Button2
Callfunction_Button2 = None

##function called in interrupt of boton 2
def Callfunction_Interrupt_Button2(pin):
    global Callfunction_Button2
    countermark = 0
    while(GPIO.input(Define.BUTTON_2)==0): ##To avoid false clicks in the button
        countermark = countermark+1
        if(countermark>=100000):
            countermark=100000
    if(countermark>=100000):
        try:
            Callfunction_Button2()
        except TypeError:
            print("Error running interrupt function, check that function doesnt have arguments or errors")


###class that controls the buttons and leds in the board
class boardbk(object):

    def __init__(self):
        self.nada=0

    ##Enable a button with interrupt sequence
    def Enable_Interrupt_Button(self,botnum,functionsaver):
        global Callfunction_Button1
        if(not(callable(functionsaver))):
            print("Last argument most be a function with no arguments")
            return(0)
        if(botnum==1):
            botnum=Define.BUTTON_1
            GPIO.setup(botnum,GPIO.IN,pull_up_down=GPIO.PUD_UP)  ##GPIO.PUD_UP,GPIO.PUD_DOWN,GPIO.PUD_OFF
            GPIO.add_event_detect(botnum,GPIO.FALLING,bouncetime=200)
            Callfunction_Button1 = functionsaver
            GPIO.add_event_callback(botnum,Callfunction_Interrupt_Button1)
        else:
            botnum=Define.BUTTON_2
            GPIO.setup(botnum,GPIO.IN,pull_up_down=GPIO.PUD_UP)  ##GPIO.PUD_UP,GPIO.PUD_DOWN,GPIO.PUD_OFF
            GPIO.add_event_detect(botnum,GPIO.FALLING,bouncetime=200)
            Callfunction_Button2 = functionsaver
            GPIO.add_event_callback(botnum,boardbk.Callfunction_Interrupt_Button2)

    ##disable interrupt from button
    def Disable_Interrupt_Button(self,botnum):
        if(botnum==1):
            botnum=Define.BUTTON_1
            GPIO.remove_event_detect(botnum)
        else:
            botnum=Define.BUTTON_2
            GPIO.remove_event_detect(botnum)

    ##enable a button only to read
    def Enable_Button(self,botnum):
        if(botnum==1):
            botnum=Define.BUTTON_1
            GPIO.setup(botnum,GPIO.IN,pull_up_down=GPIO.PUD_UP)  ##GPIO.PUD_UP,GPIO.PUD_DOWN,GPIO.PUD_OFF
        else:
            botnum=Define.BUTTON_2
            GPIO.setup(botnum,GPIO.IN,pull_up_down=GPIO.PUD_UP)  ##GPIO.PUD_UP,GPIO.PUD_DOWN,GPIO.PUD_OFF

    ##read the selected button
    def Read_Button(self,botnum):
        if(botnum==1):
            botnum=Define.BUTTON_1
        else:
            botnum=Define.BUTTON_2
        return(GPIO.input(botnum))

    ##enable a led to control
    def Enable_Led(self,lednum):
        if(lednum==1):
            lednum=Define.LED_1
            GPIO.setup(lednum,GPIO.OUT)
            GPIO.output(lednum,0)
        elif(lednum==2):
            lednum=Define.LED_2
            GPIO.setup(lednum,GPIO.OUT)
            GPIO.output(lednum,0)
        else:
            lednum=Define.LED_3
            GPIO.setup(lednum,GPIO.OUT)
            GPIO.output(lednum,0)

    ##modify led status
    def Set_Led(self,lednum,statex):
        if(statex>1):
            statex=1
        if(statex<1):
            statex=0
        if(lednum==1):
            lednum=Define.LED_1
            GPIO.output(lednum,statex)
        elif(lednum==2):
            lednum=Define.LED_2
            GPIO.output(lednum,statex)
        else:
            lednum=Define.LED_3
            GPIO.output(lednum,statex)

    ##clean up all gpio
    def CleanUp(self):
        GPIO.cleanup()


        
