from modules.common import *
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from ui import connection
# import time
# # import curses
# # from classes import *
# from ui.operations import *
# import pyautogui as pag
# # from multiprocessing import Process
# import threading
# from copy import deepcopy
# import win32
# import win32gui
# import win32.lib.win32con as win32con
# import ctypes
# import socket
# import os
# import sys

hidden = None
the_program_to_hide = ctypes.windll.kernel32.GetConsoleWindow()


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        pass
    return False

def restartprogram():
	os.execl(sys.executable, sys.executable, *sys.argv)


# screenlock = threading.Semaphore(value=1)
# screenlock = threading.Semaphore(value=1)
# screenlock.acquire()


def countdown(t, message):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
       	# screenlock.acquire()
        print(f"{message} {timeformat}", end='\r')
        # screenlock.release()
        time.sleep(1)
        t -= 1

while True:
	try:
		print("\nAuthenticating...")
		client = connection.connect()
		print("Authentication Successful!")
		break
	except:
		countdown(60, "Authentication Failed. Next Attempt to Authenticate:")

while True:		
	try:
		sheet = connection.opensheet("exterior", client)
		print("Spreadsheet opened.")
		break
	except:
		countdown(60, "Spreadsheet could not be opened. Next Attempt to Open Spreadsheet:")


class Job:
	def __init__(self, code):
		self.code = code

	def execute(self):
		exec(self.code)


processes = deepcopy(operations)

for key in list(operations['uniform'].keys()):
	processes['uniform'][key] = Job('')
	processes['uniform'][key].code=(f"""
while True:
	while refresh.proceed is True:
		if refresh.{key} == True or refresh.{key} == 'True':
			# screenlock.acquire()
			exec(operations['uniform']['{key}']["True"])
			# screenlock.release()
		elif refresh.{key} == False or refresh.{key} == 'False':
			exec(operations['uniform']['{key}']["False"])
		else:
			pass
""")
## if refresh.{key} == str({activation[0]}) or refresh.{key} == str({activation[1]}):
		
def refresh():
	refresh.proceed=False
	refresh.connected = None
	while True:

		#Checking Internet Status...
		refresh.internet = is_connected()
		if refresh.internet is False:
			refresh.proceed = False
			print("Internet Issues Detected. Restarting Program...")
			restartprogram()

		refresh.records = sheet.get_all_records()[0]
		for key in list(refresh.records.keys()):
			exec(f"refresh.{key}=refresh.records[key]")
		refresh.proceed=True
		# screenlock.acquire()
		countdown(refresh.CHECKINTERVAL, "Next Refresh:")
		# screenlock.release()

# def createprocess(key, activation):
# # for key in list(processes['uniform'].keys()):
# 	exec(f"""
# while True:
# 	while refresh.proceed is True:
# 		if refresh.{key} == str({activation[0]}) or refresh.{key} == str({activation[1]}):
# 			# screenlock.acquire()
# 			processes['uniform']['{key}'].execute()
# 			# screenlock.release()
# 		else:
# 			pass
# 	""")

def executeProcess(name):
	processes['uniform'][name].execute()


def SWITCHprocess():	
	executeProcess('SWITCH')

def STAYAWAKEprocess():
	executeProcess('STAYAWAKE')

def DEBUGMODEprocess():
	executeProcess('DEBUGMODE')

def CODEXECprocess():
	executeProcess('CODEXEC')

'''
def main():    
	while True:
		if refresh.proceed == True:
			if refresh.SWITCH == "True":
				processes['uniform']['SWITCH'].execute()
			else:
				pass

def stayawake():
	while True:
		if refresh.proceed == True:
			while refresh.STAYAWAKE == "True":
				processes['uniform']['STAYAWAKE'].execute()

if __name__=='__main__':
	threading.Thread(target = refresh).start()
	threading.Thread(target = main).start()
	threading.Thread(target = refresh).start()
'''
try:
	if __name__=='__main__':
		threading.Thread(target = refresh).start()
		threading.Thread(target = DEBUGMODEprocess).start()
		threading.Thread(target = SWITCHprocess).start()
		threading.Thread(target = STAYAWAKEprocess).start()
		threading.Thread(target = CODEXECprocess).start()
except KeyboardInterrupt:
	sys.exit()

# stdscr = curses.initscr()
# while True:
#     stdscr.erase()
#     stdscr.addstr('>>> Thread 1: ' + str(line_thread_1) + '\n')
#     stdscr.addstr('>>> Thread 2: ' + str(line_thread_2) + '\n')
#     stdscr.addstr('>>> Thread 2: ' + str(line_thread_3) + '\n')
#     stdscr.refresh()
#     time.sleep(1)
# curses.endwin()
# screenlock.release()



'''All uniform side functions will be called simulataneously and run on instruction of uniform main function
uniform side functions will use global variables to break away midway
uniform main function will run literally all the time and will call multiexecution() function
multiexecution function will multiexecute main and side functions

Uniform side functions:
DEBUGMODE
STAYAWAKE
CLOSEALL
CHECKINTERVAL 
'''