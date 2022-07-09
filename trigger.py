from modules.common import *


# hidden = None
"""Doesnt work anymore - 
# the_program_to_hide = ctypes.windll.kernel32.GetConsoleWindow()
#Initializing V100 Emulation
# kernel32 = ctypes.WinDLL('kernel32') 
# hStdOut = kernel32.GetStdHandle(-11)
# mode = ctypes.c_ulong()
# kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
# mode.value |= 4
# kernel32.SetConsoleMode(hStdOut, mode)
"""

the_program_to_hide = win32gui.GetForegroundWindow() 

os.chdir(USER_CONSTANTS.PROJECT_PATH)

ctypes.windll.kernel32.SetConsoleTitleW("MENTAL-OUT")


def end_program_from_systray(systray):
	os._exit(0)

def hide_program(systray):
	win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
hide_program(None)

def show_program(systray):
	win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)

#Adding app to system tray
menu_options = (
	("Hide Console", None, hide_program),
	("Show Console", None, show_program),)

systray = SysTrayIcon(f"favicon.ico", "MENTAL-OUT", menu_options, on_quit=end_program_from_systray)
systray.start()

#Ensuring systray gets appropriately dismantled when program ends
def exit_handler():
	systray.shutdown()

atexit.register(exit_handler)



class Exterior:
 	uniform_thread_scripts = dict()
 	processes = dict()
 	records = None


#Defining ANSI Colour Codes and MENTALOUT Header Text:
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLRSCRN = '\033c'
    MENTALOUT ='''

▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ ░█▀▀█ ▒█░░░ ░░ ▒█▀▀▀█ ▒█░▒█ ▀▀█▀▀ 
▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ ▒█▄▄█ ▒█░░░ ▀▀ ▒█░░▒█ ▒█░▒█ ░▒█░░ 
▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ ▒█░▒█ ▒█▄▄█ ░░ ▒█▄▄▄█ ░▀▄▄▀ ░▒█░░
'''

print(f'\n\n{bcolors.OKGREEN}Welcome {bcolors.HEADER}{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC} {bcolors.OKGREEN}!{bcolors.ENDC}')


class Job:
	def __init__(self, code):
		self.code = code

	def execute(self):
		exec(self.code)


class Logger():
	def __init__(self, log):
		self.log=[]
		self.log.append(log)


	def updatelog(self, text, end=None):
		if len(self.log)>5 or end=='\r':
			self.log.pop(0)
		self.log.append('\n'+bcolors.WARNING+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+':	'+bcolors.ENDC+text)

	def deletelog(self):
		while bool(len(self.log)) is True:
			self.log.pop(0)

	def getlog(self):
		totalLog=""""""
		for element in self.log:
			totalLog+=element
		return totalLog





def restartprogram():
	os.execl(sys.executable, sys.executable, *sys.argv)


def protect_connection(codetext):
	global mainlogger
	global refreshlogger
	try:
		exec(codetext)
		mainlogger.deletelog()
		mainlogger.updatelog(f'{bcolors.HEADER}{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.OKBLUE} is currently connected to {bcolors.HEADER}Exterior/{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.ENDC}')
	except:
		mainlogger.deletelog()
		refreshlogger.deletelog()
		mainlogger.updatelog(f'{bcolors.FAIL}\nALERT: \nInternet issues have been detected. \n{bcolors.HEADER}{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.FAIL} is currently disconnected from {bcolors.HEADER}Exterior/{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC} \n{bcolors.OKGREEN}Restarting program...{bcolors.ENDC}{bcolors.ENDC}')
		refresh.proceed = False
		time.sleep(5)
		restartprogram()


def countdown(t, message, logger=None):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
       	if logger==None:
        		print(f"{message} {timeformat}", end='\r')
        else:
        	exec(f"logger.updatelog('{message} {timeformat}', end='\\r')")
        time.sleep(1)
        t -= 1


while True:
	try:
		print(f"\n{bcolors.OKBLUE}Authenticating with {bcolors.HEADER}Exterior{bcolors.ENDC}...{bcolors.ENDC}")
		client = connection.connect()
		print(f"{bcolors.OKGREEN}Authentication Successful!{bcolors.ENDC}")
		break
	except:
		countdown(60, f"{bcolors.WARNING}Authentication Failed. Next Attempt to Authenticate:{bcolors.ENDC}")

while True:		
	try:
		sheet = connection.opensheet("Exterior",USER_CONSTANTS.COMPUTER_NAME, client)
		print(f"{bcolors.OKGREEN}Connected with {bcolors.HEADER}Exterior/{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.ENDC}")
		break
	except:
		countdown(60, f"{bcolors.HEADER}Exterior/{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.WARNING} could not be opened. Next Attempt:{bcolors.ENDC}")




for key in list(operations["UNIFORM"].keys()):
	Exterior.uniform_thread_scripts[key] = Job('')
	Exterior.uniform_thread_scripts[key].code=(f"""
global {key}logger
{key}logger = Logger('')
print = {key}logger.updatelog
while refresh.proceed is True:
	if Exterior.records['{key}'] == True or Exterior.records['{key}'] == 'True':
		# screenlock.acquire()
		exec(operations["UNIFORM"]['{key}']["True"])
		# screenlock.release()
	elif Exterior.records['{key}'] == False or Exterior.records['{key}'] == 'False':
		# exec(operations["UNIFORM"]['{key}']["False"])
		break
	else:
		pass
""")


mainlogger=Logger('')
refreshlogger=Logger('')
for key in list(operations["UNIFORM"].keys()):
	# print(str(key))
	exec(f"{key}logger=Logger('')")


def execute_process(name):
	Exterior.uniform_thread_scripts[name].execute()



def refresh():
	global refreshlogger
	print = refreshlogger.updatelog
	refresh.proceed=True
	refresh.connected = None
	while True:
		protect_connection('Exterior.records = sheet.get_all_records()[0]')
		for key in list(Exterior.records.keys()):
			exec(f"Exterior.{key}=Exterior.records[key]")
		# print(str(Exterior.scripts))
		# print(str(Exterior.processes))
		# print(str(list(Exterior.processes.keys())))
		for key in list(Exterior.uniform_thread_scripts.keys()):
			if Exterior.records[key] == True or Exterior.records[key] == 'True':
				if key in Exterior.processes:
					if not Exterior.processes[key].is_alive(): #Check if thread is alive
						Exterior.processes[key] = threading.Thread(target = execute_process, args=[key])
						Exterior.processes[key].start()
						Exterior.processes[key].name = key
				else:
					Exterior.processes[key] = threading.Thread(target = execute_process, args=[key])
					Exterior.processes[key].start()
					Exterior.processes[key].name = key
			elif Exterior.records[key]== False or Exterior.records[key]=='False':
				pass
			else:
				pass
# 			exec(f"""
# # print(f"entered loop")
# if(Exterior.{key}== True or Exterior.{key}=='True'):
# 	# print(f"starting {key}")
# 	if not Exterior.processes[key] in globals():
# 		Exterior.processes[key] = threading.Thread(target = execute_process, args=[key])
# 	if not Exterior.processes[key].is_alive():
# 		Exterior.processes[key].start()
# 	# print(f"started {key}")
# elif Exterior.{key}== False or Exterior.{key}=='False':
# 	pass
# else:
# 	pass
# """)
		refresh.proceed=True
		countdown(Exterior.CHECKINTERVAL, f"{bcolors.OKGREEN}Next Request In:{bcolors.ENDC}", logger=refreshlogger)


def displaylog():

	displaylog.thisloggerlog=None
	displaylog.toprint=""""""

	global refreshlogger
	global mainlogger

	for key in list(operations["UNIFORM"].keys()):
		exec(f"""
global {key}logger
""")

	while True:

		displaylog.toprint=""""""

		for key in list(operations["UNIFORM"].keys()):
			if Exterior.records != None:	
				if Exterior.records[key] == True or Exterior.records[key] == 'True':
					exec(f"""
displaylog.thisloggerlog = {key}logger.getlog()
""")		
					displaylog.toprint+=(f"""
{bcolors.OKBLUE}PARAMETER:{bcolors.ENDC} {bcolors.OKGREEN}{key}{bcolors.ENDC} 
{displaylog.thisloggerlog}
\n
""")
		time.sleep(1)

		print(f"""
{bcolors.CLRSCRN}
{bcolors.HEADER}{bcolors.MENTALOUT}{bcolors.ENDC}
{bcolors.HEADER}Welcome {USER_CONSTANTS.COMPUTER_NAME} !{bcolors.ENDC}
{mainlogger.getlog()} 
{refreshlogger.getlog()}
\n\n
{displaylog.toprint}

{bcolors.HEADER}CACHE LOGS:{bcolors.ENDC}
""")
		


refresh_process = threading.Thread(target = refresh)

displaylog_process = threading.Thread(target = displaylog)

if __name__ == '__main__':    
	refresh_process.start()
	displaylog_process.start()
