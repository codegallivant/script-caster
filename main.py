from src.common import *



the_program_to_hide = win32gui.GetForegroundWindow() 

os.chdir(USER_CONSTANTS.PROJECT_PATH)

ctypes.windll.kernel32.SetConsoleTitleW("MENTAL-OUT")


def end_program_from_systray(systray):
    os._exit(0)

def hide_program(systray):
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
# hide_program(None)

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
     records = dict()
     processes = dict()
     process_loggers = dict()
     all_sheet_values = list()


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
        self.log.append('\n'+bcolors.WARNING+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+':    '+bcolors.ENDC+text)

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
        client = exterior_connection.authenticate('creds/service_account_credentials.json')
        print(f"{bcolors.OKGREEN}Authentication Successful!{bcolors.ENDC}")
        break
    except:
        countdown(60, f"{bcolors.WARNING}Authentication Failed. Next Attempt to Authenticate:{bcolors.ENDC}")

while True:        
    try:
        sheet = exterior_connection.open_sheet("Exterior",USER_CONSTANTS.COMPUTER_NAME, client)
        print(f"{bcolors.OKGREEN}Connected with {bcolors.HEADER}Exterior/{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.ENDC}")
        break
    except:
        countdown(60, f"{bcolors.HEADER}Exterior/{USER_CONSTANTS.COMPUTER_NAME}{bcolors.ENDC}{bcolors.WARNING} could not be opened. Next Attempt:{bcolors.ENDC}")


def update_local_user_scripts():
    user_scripts_list = user_scripts_compiler.update_scripts(USER_CONSTANTS.ACCESS_TOKEN, USER_CONSTANTS.USERNAME, USER_CONSTANTS.OPS_REPO_NAME, f"{USER_CONSTANTS.PROJECT_PATH}/local_user_scripts")
    return  user_scripts_list

while True:
    try: 
        print(f"\n{bcolors.OKBLUE}Fetching user-scripts from {bcolors.HEADER}GitHub/{USER_CONSTANTS.USERNAME}/{USER_CONSTANTS.OPS_REPO_NAME}{bcolors.ENDC}...{bcolors.ENDC}")
        user_scripts_list = update_local_user_scripts()
        break
    except:
        countdown(60, f"{bcolors.WARNING}Failed to fetch user-scripts from {bcolors.HEADER}GitHub/{USER_CONSTANTS.USERNAME}/{USER_CONSTANTS.OPS_REPO_NAME}{bcolors.ENDC}.{bcolors.WARNING} Next Attempt:{bcolors.ENDC}")


mainlogger=Logger('')
refreshlogger=Logger('')
for key in user_scripts_list:
    Exterior.process_loggers[key] = Logger('')



def refresh():
    global refreshlogger
    print = refreshlogger.updatelog
    global sheet
    global user_scripts_list

    while True:
        
        protect_connection(f'Exterior.all_sheet_values, Exterior.records = exterior_connection.get_parameter_cell_values(sheet)')

        if Exterior.records["UPDATE_LOCAL_USER_SCRIPTS"] == "ON":
            
            print(f"{bcolors.OKBLUE}Updating {bcolors.HEADER}user-scripts{bcolors.ENDC}...", end='\r')
            
            try:
            	user_scripts_list = update_local_user_scripts()
            	protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, 'UPDATE_LOCAL_USER_SCRIPTS', 'Done ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', 'result', Exterior.all_sheet_values)")
            except:
            	print(f"{bcolors.HEADER}User-scripts {bcolors.OKGREEN}updated{bcolors.ENDC}.", end='\r')
            	protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, 'UPDATE_LOCAL_USER_SCRIPTS', 'Failed ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', 'result', Exterior.all_sheet_values)")
            
            protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, 'UPDATE_LOCAL_USER_SCRIPTS', 'OFF', 'status', Exterior.all_sheet_values)")

        for key in user_scripts_list:
            
            if key in Exterior.records:
                
                if Exterior.records[key] == 'ON':
                    
                    if key in Exterior.processes:  #Element exists 
                        
                        if Exterior.processes[key].poll() != None: #Thread is not running
                          
                            protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, '{key}', 'OFF', 'status', Exterior.all_sheet_values)")
                          
                            if Exterior.processes[key].poll() == 0:
                                protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, '{key}', 'Done ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', 'result', Exterior.all_sheet_values)")
                            else:
                                protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, '{key}', 'Failed ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', 'result', Exterior.all_sheet_values)")

                            del Exterior.processes[key]

                    else: # Element doesnt exist
            
                        new_env = os.environ.copy()
                        new_env["PYTHONPATH"]=USER_CONSTANTS.PROJECT_PATH
                        new_env["PYTHONUNBUFFERED"] = "1"
                        Exterior.processes[key] = subprocess.Popen(["python", f"{USER_CONSTANTS.PROJECT_PATH}/local_user_scripts/user_script_files/{key}.py"], cwd = USER_CONSTANTS.PROJECT_PATH, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, env=new_env)
            
                        protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, '{key}', 'Running ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', 'result', Exterior.all_sheet_values)")
            
                elif Exterior.records[key]=='OFF':
            
                    if key in Exterior.processes:
                        if Exterior.processes[key].poll() == None: #Thread is running
                            protect_connection(f"exterior_connection.update_parameter_cell_value(sheet, '{key}', 'Done ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', 'result', Exterior.all_sheet_values)")
                            #Kill process
                            Exterior.processes[key].terminate()
                        del Exterior.processes[key]
            
                else:
                    pass
        
        countdown(int(Exterior.records["REQUEST_INTERVAL"]), f"{bcolors.OKGREEN}Next Request In:{bcolors.ENDC}", logger=refreshlogger)



def update_loggers():
    while True:
        for key in user_scripts_list:
            if key in list(Exterior.processes.keys()):
                if Exterior.processes[key].poll() == None: #process is running
                    output = Exterior.processes[key].stdout.readline()
                    if not output:
                        continue
                    else:
                        Exterior.process_loggers[key].updatelog(str(output))


def displaylog():

    displaylog.thisloggerlog=None
    displaylog.toprint=""""""

    global refreshlogger
    global mainlogger

    while True:

        displaylog.toprint=""""""

        for key in user_scripts_list:
            if len(Exterior.records)>0:    
                if Exterior.records[key] == 'ON':
                    displaylog.thisloggerlog = Exterior.process_loggers[key].getlog()
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

update_loggers_process = threading.Thread(target = update_loggers)

displaylog_process = threading.Thread(target = displaylog)



if __name__ == '__main__':    
    refresh_process.start()
    update_loggers_process.start()
    displaylog_process.start()

