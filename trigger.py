import gspread
from oauth2client.service_account import ServiceAccountCredentials
import connection
import time
# from classes import *
from operations import *
import pyautogui as pag
# from multiprocessing import Process
import threading
from copy import deepcopy


# screenlock = threading.Semaphore(value=1)
# screenlock.acquire()


def countdown(t, message):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"{message} {timeformat}", end='\r')
        time.sleep(1)
        t -= 1

while True:
	try:
		print("Authenticating...")
		client = connection.connect()
		print("Authentication Successful!")
		break
	except:
		print("Authentication Failed.")
		countdown(60, "Next Attempt to Authenticate:", end="\r")

while True:		
	try:
		sheet = connection.opensheet("exterior", client)
		print("Spreadsheet opened.")
		break
	except:
		print("Spreadsheet could not be opened.", , end="\r")
		countdown(60, "Next Attempt to Open Spreadsheet:")


class Job:
	def __init__(self, code):
		self.code = code

	def execute(self):
		exec(self.code)


processes = deepcopy(operations)

for key in list(operations['uniform'].keys()):
	processes['uniform'][key] = Job('')
	processes['uniform'][key].code=operations['uniform'][key]

def refresh():
	refresh.proceed=False
	while True:
		for key in list(processes['uniform'].keys()):
			exec(f"refresh.{key}=sheet.get_all_records()[0][key]")
		refresh.proceed=True
		countdown(refresh.CHECKINTERVAL, "Next Refresh:")

def createprocess(key):
# for key in list(processes['uniform'].keys()):
	exec(f"""
while True:
	if refresh.proceed == True:
		if refresh.{key} == "True" or refresh.{key} == True :
			processes['uniform']['{key}'].execute()
		else:
			pass
	""")

def SWITCHprocess():	
	createprocess("SWITCH")

def STAYAWAKEprocess():
	createprocess("STAYAWAKE")
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
if __name__=='__main__':
	threading.Thread(target = refresh).start()
	threading.Thread(target = SWITCHprocess).start()
	threading.Thread(target = STAYAWAKEprocess).start()

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