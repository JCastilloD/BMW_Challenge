import sys
sys.path.append("/home/pi/bmw/libs")
import boardIObk as board
import time

board1 = board.boardbk()
board1.Enable_Led(1)
board1.Set_Led(1,1)
time.sleep(1)
board1.Set_Led(1,0)
time.sleep(1)
board1.CleanUp()
