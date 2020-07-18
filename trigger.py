from modules.common import *


hidden = None
the_program_to_hide = ctypes.windll.kernel32.GetConsoleWindow()

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
		self.log.append('\n'+text)


	def getlog(self):
		totalLog=""""""
		for element in self.log:
			totalLog+=element
		return totalLog



def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        pass
    return False


def restartprogram():
	os.execl(sys.executable, sys.executable, *sys.argv)


def protectDisconnect(codetext):
	try:
		exec(codetext)
	except:
		exec(f"refreshlogger.updatelog('{bcolors.FAIL}Internet Issues Detected. Restarting Program...{bcolors.ENDC}')")
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
		print(f"\n{bcolors.OKBLUE}Authenticating...{bcolors.ENDC}")
		client = connection.connect()
		print(F"{bcolors.OKGREEN}Authentication Successful!{bcolors.ENDC}")
		break
	except:
		countdown(60, f"{bcolors.WARNING}Authentication Failed. Next Attempt to Authenticate:{bcolors.ENDC}")

while True:		
	try:
		sheet = connection.opensheet("exterior", client)
		print(f"{bcolors.OKGREEN}Spreadsheet opened.{bcolors.ENDC}")
		break
	except:
		countdown(60, f"{bcolors.WARNING}Spreadsheet could not be opened. Next Attempt to Open Spreadsheet:{bcolors.ENDC}")


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
		protectDisconnect('Exterior.records = sheet.get_all_records()[0]')
		for key in list(Exterior.records.keys()):
			exec(f"Exterior.{key}=Exterior.records[key]")
		refresh.proceed=True
		countdown(Exterior.CHECKINTERVAL, "Next Request In:", logger=refreshlogger)


def displaylog():

	displaylog.thisloggerlog=None
	displaylog.toprint=""""""

	global refreshlogger

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
{bcolors.HEADER}
{bcolors.MENTALOUT}
{bcolors.ENDC} {bcolors.OKGREEN}{refreshlogger.getlog()}{bcolors.ENDC}
\n\n
{displaylog.toprint}
""")
		

def executeProcess(name):
	processes['uniform'][name].execute()

def main():
	threading.Thread(target = refresh).start()
	for key in list(processes['uniform']):
		print(key)
		threading.Thread(target = executeProcess, args=[key]).start()
	threading.Thread(target = displaylog).start()

main()
