import sys
sys.path.append("/home/pi/bmw/libs")
import boardIObk as board
import time

def End_All_Callable():
    board1.Disable_Interrupt_Button(1)
    board1.CleanUp()
    print("interrupts disabled")
    sys.exit("interrupt trigger")

board1 = board.boardbk()
board1.Enable_Interrupt_Button(1,End_All_Callable)
while(1):
    time.sleep(0.1)
