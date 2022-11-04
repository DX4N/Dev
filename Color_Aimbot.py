from random import gammavariate
from PIL import Image
import pyautogui
from time import sleep
import time
import sys
import win32gui, win32api, win32con, ctypes

# Enemy Color
color = (255, 0, 0) # (R, G, B)

xCord = 960 # 1920
yCord = 540 # 1080

# Default Box 640x360
Box = 640, 360, 640, 360

def main():

	while(True):
		cmd = input(" Command>")
		cmd = cmd.lower()
		if cmd == "help":
			print (
    """\nList of commands:\n  
	help - Displays a List of Commands
	info - Displays Aimbot Information
	aimbot.on - Activate the Aimbot
	shotbot.on - Activate the Shotbot
	resolution.setup - Monitor Resolution Settings
	exit - Exit this Script\n"""
                  )

		elif cmd == "aimbot.on":
			Aimbot_GO()

		elif cmd == "exit":
			sys.exit()

		elif cmd == "shotbot.on":
			print("\n To be finished later...\n")

		elif cmd == "debug":
			debug_mode()

		elif cmd == "info":
			print(
                    """
                    Perfect Aimbot for any Game:
  	                - Auto-Aim Tool Designed using in-game enemy pixel color detection.
  	                - Unique logic that enables amazing speed and accuracy.
                    """
                 )

def Aimbot_GO():
    
    while(True):
        x,y = win32api.GetCursorPos()
        pic = pyautogui.screenshot(region=(Box))
        pix_val = list(pic.getdata())

        if color in pix_val:
            xCord = pix_val.index(color) /640
            yCord = pix_val.index(color) %640

            if(yCord>310):
                z = (yCord - 310) /2
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,z,0,0,0)

            elif(yCord<310):
                z = (310 - yCord) / 2
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,-(z),0,0,0)

            if(xCord>100):
                x = (xCord - 100) /2
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,x,0,0)

            elif(xCord<100):
                x = (100 - xCord) /2
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,-(x),0,0)

        else:
                pass


def Shotbot_GO():
        try:
            while True:
                pixleColor = pyautogui.screenshot().getpixle((1025, 561))
                time.sleep(0)

                if (str(color[0]).rjust(3) == "220" and str(color[1]).rjust(3) == " 12" and str(color[2]).rjust(3) == " 14"):
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                                sleep(0.05)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

        except KeyboardInterrupt:
            print("Done.")


def print_no_newline(string):
	import sys
	sys.stdout.write("\r")
	sys.stdout.write(string)
	sys.stdout.flush()


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def debug_mode():
    while(True):
        pic = pyautogui.screenshot(region=(Box))
        pix_val = list(pic.getdata())

        if color in pix_val:
            xCord = pix_val.index(color) / 640
            yCord = pix_val.index(color) % 640

main()
