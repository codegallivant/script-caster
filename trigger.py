from modules.common import *


hidden = None
the_program_to_hide = ctypes.windll.kernel32.GetConsoleWindow()
computer_name = socket.gethostname()

#Initializing V100 Emulation
kernel32 = ctypes.WinDLL('kernel32') 
hStdOut = kernel32.GetStdHandle(-11)
mode = ctypes.c_ulong()
kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
mode.value |= 4
kernel32.SetConsoleMode(hStdOut, mode)


class Exterior:
 	pass


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

print(f'\n\n{bcolors.OKGREEN}Welcome {bcolors.HEADER}{computer_name}{bcolors.ENDC} {bcolors.OKGREEN}!{bcolors.ENDC}')


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
		while len(self.log):
			self.log.pop(0)

	def getlog(self):
		totalLog=""""""
		for element in self.log:
			totalLog+=element
		return totalLog


def restartprogram():
	os.execl(sys.executable, sys.executable, *sys.argv)


def protectConnection(codetext):
	global mainlogger
	global refreshlogger
	try:
		exec(codetext)
		mainlogger.deletelog()
		mainlogger.updatelog(f'{bcolors.HEADER}{computer_name}{bcolors.ENDC}{bcolors.OKBLUE} is currently connected to {bcolors.HEADER}Exterior/{computer_name}{bcolors.ENDC}{bcolors.ENDC}')
	except:
		mainlogger.deletelog()
		refreshlogger.deletelog()
		mainlogger.updatelog(f'{bcolors.FAIL}\nALERT: \nInternet issues have been detected. \n{bcolors.HEADER}{computer_name}{bcolors.ENDC}{bcolors.FAIL} is currently disconnected from {bcolors.HEADER}Exterior/{computer_name}{bcolors.ENDC} \n{bcolors.OKGREEN}Restarting Program...{bcolors.ENDC}{bcolors.ENDC}')
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
		print(F"{bcolors.OKGREEN}Authentication Successful!{bcolors.ENDC}")
		break
	except:
		countdown(60, f"{bcolors.WARNING}Authentication Failed. Next Attempt to Authenticate:{bcolors.ENDC}")

while True:		
	try:
		sheet = connection.opensheet("Exterior",computer_name, client)
		print(f"{bcolors.OKGREEN}Connected with {bcolors.HEADER}Exterior/{computer_name}{bcolors.ENDC}{bcolors.ENDC}")
		break
	except:
		countdown(60, f"{bcolors.HEADER}Exterior/{computer_name}{bcolors.ENDC}{bcolors.WARNING} could not be opened. Next Attempt:{bcolors.ENDC}")


processes = deepcopy(operations)

for key in list(operations['uniform'].keys()):
	processes['uniform'][key] = Job('')
	processes['uniform'][key].code=(f"""
global {key}logger
{key}logger = Logger('')
print = {key}logger.updatelog
while True:
	while refresh.proceed is True:
		if Exterior.{key} == True or Exterior.{key} == 'True':
			# screenlock.acquire()
			exec(operations['uniform']['{key}']["True"])
			# screenlock.release()
		elif Exterior.{key} == False or Exterior.{key} == 'False':
			exec(operations['uniform']['{key}']["False"])
		else:
			pass
""")

mainlogger=Logger('')
refreshlogger=Logger('')

for key in list(operations['uniform'].keys()):
	exec(f"{key}logger=Logger('')")


def refresh():
	global refreshlogger
	print = refreshlogger.updatelog
	refresh.proceed=False
	refresh.connected = None
	Exterior.records = None
	while True:
		protectConnection('Exterior.records = sheet.get_all_records()[0]')
		for key in list(Exterior.records.keys()):
			exec(f"Exterior.{key}=Exterior.records[key]")
		refresh.proceed=True
		countdown(Exterior.CHECKINTERVAL, f"{bcolors.OKGREEN}Next Request In:{bcolors.ENDC}", logger=refreshlogger)


def displaylog():

	displaylog.thisloggerlog=None
	displaylog.toprint=""""""

	global refreshlogger
	global mainlogger

	for key in list(operations['uniform'].keys()):
		exec(f"""
global {key}logger
""")

	while True:

		time.sleep(1)

		displaylog.toprint=""""""

		for key in list(operations['uniform'].keys()):
			exec(f"""
displaylog.thisloggerlog = {key}logger.getlog()
""")		

			displaylog.toprint+=(f"""
{bcolors.OKBLUE}PARAMETER:{bcolors.ENDC} {bcolors.OKGREEN}{key}{bcolors.ENDC} 
{displaylog.thisloggerlog}
\n
""")

		print(f"""
{bcolors.CLRSCRN}
{bcolors.HEADER}{bcolors.MENTALOUT}{bcolors.ENDC}
{bcolors.HEADER}Welcome {computer_name} !{bcolors.ENDC}
{mainlogger.getlog()} 
{refreshlogger.getlog()}
\n\n
{displaylog.toprint}
""")
		

def executeProcess(name):
	processes['uniform'][name].execute()


def main():
	threading.Thread(target = refresh).start()
	for key in list(processes['uniform']):
		threading.Thread(target = executeProcess, args=[key]).start()
	threading.Thread(target = displaylog).start()


main()
