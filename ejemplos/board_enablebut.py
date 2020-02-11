import sys
sys.path.append("/home/pi/bmw/libs")
import boardIObk as board
import time

board1 = board.boardbk()
board1.Enable_Button(1)
while(1):
    if(board1.Read_Button(1)==0):
        board1.CleanUp()
        print("GPIO clean")
        sys.exit("interrupt trigger")
    time.sleep(0.1)
