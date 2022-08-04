from src.common import *



os.chdir(USER_CONSTANTS.PROJECT_PATH)

ctypes.windll.kernel32.SetConsoleTitleW("ScriptCaster")


root = tk.Tk()

# Import the tcl file with the tk.call method
root.tk.call('source', 'tkthemes/azure-ttk-theme/azure.tcl')  # Put here the path of your theme file
root.tk.call("set_theme", "dark")
# # Set the theme with the theme_use method
# style.theme_use('azure')  # Theme files create a ttk theme, here you can put its name


class AutoScrollbar(tk.ttk.Scrollbar): # Custom class is used so that scrollbar autohides itself when not needed
       
    # Defining set method with all 
    # its parameter
    def set(self, low, high):
           
        if float(low) <= 0.0 and float(high) >= 1.0:
               
            # Using grid_remove
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        tk.ttk.Scrollbar.set(self, low, high)
       
    # Defining pack method
    def pack(self, **kw):
           
        # If pack is used it throws an error
        raise (TclError,"pack cannot be used with \
        this widget")
       
    # Defining place method
    def place(self, **kw):
           
        # If place is used it throws an error
        raise (TclError, "place cannot be used  with \
        this widget")



root.title(f"ScriptCaster")
root.iconbitmap('favicon.ico')
# root.geometry("680x300")
root.resizable(0,0)

# title_section = tk.ttk.Frame(root)
# title_section.grid(row =1,column=0, columnspan=2)
# title = tk.ttk.Label(title_section, text =  "Log", font = ("Segoe UI bold", 15))
# title.pack()

desc_section = tk.ttk.LabelFrame(root)
desc_section.grid(row=2,column=0, columnspan=2, sticky="ew", padx=15, pady=15, ipady=10)
desc_text_strvar1 = tk.StringVar()
desc_text1 = tk.Label(desc_section, textvariable = desc_text_strvar1, justify='left', wraplength=800, padx=5, pady=5)
desc_text1.grid(row=1,column=1, sticky="w")
desc_text_strvar2 = tk.StringVar()
desc_text2 = tk.Label(desc_section, textvariable = desc_text_strvar2, justify='left', wraplength=800, padx=5, pady=5)
desc_text2.grid(row=2,column=1, sticky="w")

chosen_log = tk.StringVar()
chosen_log.set("Choose a script")

ops_treeview_section = tk.ttk.Frame(root)
ops_treeview_section.grid(row=3,column=0,sticky="ns", padx=15)

ops_treeview = tk.ttk.Treeview(ops_treeview_section, selectmode = "browse", height=18)
ops_treeview["columns"]=("Scripts")
ops_treeview["show"]="headings"
ops_treeview.heading("Scripts",text = "Scripts")
ops_treeview.tag_configure('Done', background='green')
ops_treeview.tag_configure('Running', background='orange')
ops_treeview.tag_configure('Failed', background='red')
ops_treeview.tag_configure('None', background='')

ops_treeview_scrollbar = AutoScrollbar(ops_treeview_section, orient="vertical", command = ops_treeview.yview)

ops_treeview.config(yscrollcommand = ops_treeview_scrollbar.set)

ops_treeview.grid(row=1, column=1,sticky="ns")
ops_treeview_scrollbar.grid(row=1,column=2,sticky="ns")


ops_log_section = tk.ttk.LabelFrame(root, text = "Choose a script")
# ops_log_section.configure(text = chosen_log) whenever you want
ops_log_section.grid(row=3,column=1, sticky='nsew', padx=15)

ops_log = tk.Text(ops_log_section, borderwidth=0)
ops_log.configure(state="disabled")
ops_log_section_xscrollbar = AutoScrollbar(ops_log_section, orient = "horizontal", command=ops_log.xview)
ops_log_section_yscrollbar = AutoScrollbar(ops_log_section, orient = "vertical", command=ops_log.yview)
ops_log.config(xscrollcommand=ops_log_section_xscrollbar.set, yscrollcommand=ops_log_section_yscrollbar.set)

ops_log.grid(row=1,column=1, sticky='nsew')
ops_log_section_xscrollbar.grid(row=2, column=1, sticky='ew')
ops_log_section_yscrollbar.grid(row=1,column=2, sticky='ns')




def restart_program_fromTkWin():
    root.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv)

def quit_window_fromTkWin():
    root.destroy()
    os._exit(0)


def restart_program_fromSysTray(icon, item):
    icon.stop()
    root.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv)

def quit_window_fromSysTray(icon, item):
    icon.stop()
    root.destroy()
    os._exit(0)

def show_window(icon, item):
    icon.stop()
    root.deiconify()


im = PIL.Image.open("favicon.ico")
systrayicon_menu = pystray.Menu(
    pystray.MenuItem(
        'Show log', 
        show_window,
        default=True),
    pystray.MenuItem(
        'Restart', 
        restart_program_fromSysTray),
    pystray.MenuItem(
        'Quit',
        quit_window_fromSysTray))


def withdraw_window():  
    root.withdraw()
    icon = pystray.Icon("script-caster-icon",im,"ScriptCaster", menu=systrayicon_menu)
    icon.run()


final_button_section = tk.Frame(root)
withdraw_button = tk.ttk.Button(final_button_section, text = 'Close', command = withdraw_window)
quit_button = tk.ttk.Button(final_button_section, text = 'Quit', command = quit_window_fromTkWin)
restart_button = tk.ttk.Button(final_button_section, text = 'Restart', command = restart_program_fromTkWin)
final_button_section.grid(row=4, column=1, sticky="e",padx=15,pady=15)
withdraw_button.pack(side="right", padx=5, pady=10)
quit_button.pack(side="right", padx=5, pady=10)
restart_button.pack(side="right", padx=5, pady=10)


footer_section = tk.Frame(root)
threadcount_strvar = tk.StringVar()
footer_name_label = tk.Label(footer_section, text = f"{USER_CONSTANTS.COMPUTER_NAME}", borderwidth=1, relief="solid", padx=2)
footer_threadcount_label = tk.Label(footer_section, textvariable=threadcount_strvar, borderwidth=1, relief="solid", padx=2)
footer_section.grid(row=5, column=0, columnspan=2, sticky="ew")
footer_threadcount_label.pack(side="right")
footer_name_label.pack(side="right")





class Exterior:
    records = dict()
    # processes = dict()
    # process_loggers = dict()
    all_sheet_values = list()


class UserScripts:
    statuses = dict()
    class ActiveSubprocesses:
        processes = dict()
        loggers = dict() 



class Logger():
    def __init__(self, log):
        self.log=[]
        self.log.append(log)


    def updatelog(self, text, end=None):
        if USER_CONSTANTS.MAX_LOG_LENGTH != None:
            if len(self.log)==USER_CONSTANTS.MAX_LOG_LENGTH:
                self.log.pop(0)
        if end=='\r' and len(self.log)>0:
            self.log.pop()
        self.log.append(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+" -"+"\n\n"+text)

    def deletelog(self):
        self.log.clear()

    def getlog(self):
        totalLog=""""""
        for element in self.log:
            totalLog+=element+"\n\n\n"
        return totalLog


mainlogger1 = Logger('')
mainlogger2 = Logger('')



def countdown(t, message, logger=None):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        if logger==None:
            print(f"{message} {timeformat}", end='\r')
        else:
            # exec(f"logger.updatelog('{message} {timeformat}', '\\r')")
            logger.updatelog(message +' '+ timeformat, end='\r')
        time.sleep(1)
        t -= 1



REMOTE_SERVER = "one.one.one.one"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except Exception:
     pass # we ignore any errors, returning False
  return False


def protect_connection(codetext):
    global mainlogger1
    global mainlogger2
    while True:
        try:
            exec(codetext)
            mainlogger1.deletelog()
            mainlogger1.updatelog(f'{USER_CONSTANTS.COMPUTER_NAME} is currently connected to Exterior/{USER_CONSTANTS.COMPUTER_NAME}')
            break
        except:
            mainlogger1.deletelog()
            mainlogger2.deletelog()
            mainlogger2.updatelog(f'An error occurred.')
            while True:
                if is_connected(REMOTE_SERVER):
                    break
                else:
                    mainlogger1.updatelog("Internet connection lost.")
                    countdown(60, "Next attempt to connect: ", logger = mainlogger2)



def insert_listitems_func(user_scripts_names):
    insert_listitems_func.finished = False
    for item in ops_treeview.get_children():
        ops_treeview.delete(item)
    for user_script_name in user_scripts_names:
        ops_treeview.insert('', index = "end",iid=user_script_name, values=(user_script_name))
    insert_listitems_func.finished = True

insert_listitems_func.finished = True

def update_local_user_scripts():
    user_scripts_names = user_scripts_compiler.update_scripts(USER_CONSTANTS.ACCESS_TOKEN, USER_CONSTANTS.USERNAME, USER_CONSTANTS.OPS_REPO_NAME, f"{USER_CONSTANTS.PROJECT_PATH}/local_user_scripts")
    threading.Thread(target = insert_listitems_func, args = [user_scripts_names]).start()
    # while insert_listitems_func.finished is False:
    #     time.sleep(1)
    user_scripts_statuses = dict()
    for user_script_name in user_scripts_names:
        user_scripts_statuses[user_script_name] = 'None'
    return  user_scripts_statuses



def main():
    
    global mainlogger1
    global mainlogger2
    
    global sheet
    
    global process_log_extractor_thread

    mainlogger1.updatelog(f'Welcome {USER_CONSTANTS.COMPUTER_NAME} !')

    while True:
        try:
            mainlogger1.updatelog(f"Authenticating with Exterior...")
            client = exterior_connection.authenticate('creds/service_account_credentials.json')
            mainlogger1.updatelog(f"Done.")
            break
        except:
            countdown(60, f"Authentication Failed. Next Attempt to Authenticate:", logger = mainlogger1)


    while True:        
        try:
            sheet = exterior_connection.open_sheet('Exterior',USER_CONSTANTS.COMPUTER_NAME, client)
            mainlogger1.updatelog(f"Connected with Exterior/{USER_CONSTANTS.COMPUTER_NAME}")
            break
        except:
            countdown(60, f"Exterior/{USER_CONSTANTS.COMPUTER_NAME} could not be opened. Next Attempt:", logger = mainlogger1)


    while True:
        try:
            mainlogger1.updatelog(f"Fetching user-scripts from GitHub/{USER_CONSTANTS.USERNAME}/{USER_CONSTANTS.OPS_REPO_NAME}...")
            UserScripts.statuses = update_local_user_scripts()
            mainlogger1.updatelog(f"Done.")
            break
        except:
            countdown(60, f"Failed to fetch user-scripts from GitHub/{USER_CONSTANTS.USERNAME}/{USER_CONSTANTS.OPS_REPO_NAME}. Next Attempt:", logger = mainlogger1)


    for key in UserScripts.statuses.keys():
        UserScripts.ActiveSubprocesses.loggers[key] = Logger('')

    


    while True:                

        protect_connection(f'Exterior.all_sheet_values, Exterior.records = exterior_connection.get_parameter_values(sheet)')

        protect_connection(f"exterior_connection.update_parameter_value(sheet,'LAST_CONTACT_TIME', datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%Y %H:%M:%S'), Exterior.all_sheet_values)")


        if Exterior.records["UPDATE_LOCAL_USER_SCRIPTS"] == "ON":
            
            mainlogger2.updatelog(f"Updating user-scripts...", end='\r')
            
            try:
                UserScripts.statuses = update_local_user_scripts()
                mainlogger2.updatelog(f"User-scripts updated.", end='\r')
                protect_connection(f"exterior_connection.update_parameter_status(sheet, 'UPDATE_LOCAL_USER_SCRIPTS', 'Done ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', Exterior.all_sheet_values)")
            except:
                mainlogger2.updatelog("Could not update user-scripts.", end='\r')
                protect_connection(f"exterior_connection.update_parameter_status(sheet, 'UPDATE_LOCAL_USER_SCRIPTS', 'Failed ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', Exterior.all_sheet_values)")
            
            protect_connection(f"exterior_connection.update_parameter_value(sheet, 'UPDATE_LOCAL_USER_SCRIPTS', 'OFF', Exterior.all_sheet_values)")

        for key in UserScripts.statuses.keys():
            
            if key in Exterior.records:
                
                if Exterior.records[key] == 'ON':
                    
                    if key in UserScripts.ActiveSubprocesses.processes.keys():  #Element exists 
                        
                        if UserScripts.ActiveSubprocesses.processes[key].poll() != None: #Thread is not running
                          
                            protect_connection(f"exterior_connection.update_parameter_value(sheet, '{key}', 'OFF', Exterior.all_sheet_values)")
                          
                            if UserScripts.ActiveSubprocesses.processes[key].poll() == 0:

                                protect_connection(f"exterior_connection.update_parameter_status(sheet, '{key}', 'Done ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', Exterior.all_sheet_values)")
                                UserScripts.statuses[key]="Done"
                            else:
                                protect_connection(f"exterior_connection.update_parameter_status(sheet, '{key}', 'Failed ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', Exterior.all_sheet_values)")
                                UserScripts.statuses[key]="Failed"
                            del UserScripts.ActiveSubprocesses.processes[key]

                    else: # Element doesnt exist
            
                        new_env = os.environ.copy()
                        new_env["PYTHONPATH"]=USER_CONSTANTS.PROJECT_PATH
                        new_env["PYTHONUNBUFFERED"] = "1"
                        extension = os.path.splitext(key)[1]
                        if extension == '.py':
                            UserScripts.ActiveSubprocesses.processes[key] = subprocess.Popen(["python",f"{USER_CONSTANTS.PROJECT_PATH}/local_user_scripts/user_script_files/{key}"], cwd = USER_CONSTANTS.PROJECT_PATH, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, env=new_env)
                        elif extension == '.pyw':
                            UserScripts.ActiveSubprocesses.processes[key] = subprocess.Popen(["pythonw",f"{USER_CONSTANTS.PROJECT_PATH}/local_user_scripts/user_script_files/{key}"], cwd = USER_CONSTANTS.PROJECT_PATH, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, env=new_env)
                        
                        protect_connection(f"exterior_connection.update_parameter_status(sheet, '{key}', 'Running ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', Exterior.all_sheet_values)")
                        UserScripts.statuses[key]="Running"
                elif Exterior.records[key]=='OFF':
            
                    if key in UserScripts.ActiveSubprocesses.processes.keys():
                        if UserScripts.ActiveSubprocesses.processes[key].poll() == None: #Thread is running
                            protect_connection(f"exterior_connection.update_parameter_status(sheet, '{key}', 'Done ({datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S')})', Exterior.all_sheet_values)")
                            UserScripts.statuses[key]="Done"
                            #Kill process
                            UserScripts.ActiveSubprocesses.processes[key].terminate()
                        del UserScripts.ActiveSubprocesses.processes[key]                    
                    else:
                        UserScripts.statuses[key]="None"

                else:
                    pass
        if UserScripts.ActiveSubprocesses.processes:
            if not process_log_extractor_thread.is_alive():
                process_log_extractor_thread = threading.Thread(target = process_log_extractor)
                process_log_extractor_thread.start()

        
        countdown(int(Exterior.records["REQUEST_INTERVAL"]), f"Next request in:", logger=mainlogger2)




def process_log_extractor():
    while UserScripts.ActiveSubprocesses.processes:
        for key in UserScripts.statuses.keys():
            if key in list(UserScripts.ActiveSubprocesses.processes.keys()):
                if UserScripts.ActiveSubprocesses.processes[key].poll() == None: #process is running
                    output = UserScripts.ActiveSubprocesses.processes[key].stdout.readline()
                    if not output:
                        continue
                    else:
                        UserScripts.ActiveSubprocesses.loggers[key].updatelog(str(output))




def show_selected_log():

    threadcount_strvar.set(f"Threads: {threading.active_count()}")

    if len(mainlogger1.log)>0:
        desc_text_strvar1.set(mainlogger1.log[-1])
    else: 
        desc_text_strvar1.set('')
        # desc_text1.delete("1.0","end")   
        # desc_text1.insert("1.0", mainlogger1.log[-1])

  
    if len(mainlogger2.log)>0:
        desc_text_strvar2.set(mainlogger2.log[-1])
    else:
        desc_text_strvar2.set('')
        # desc_text2.delete("1.0","end")   
        # desc_text2.insert("1.0", mainlogger2.log[-1])

  
    selection_list = ops_treeview.item(ops_treeview.focus())['values']
    
    if len(selection_list)>0:
        selection = selection_list[0] 
        chosen_log.set(selection)
        ops_log_section.configure(text = selection)
        yscrollbar_posn = ops_log.yview()
        xscrollbar_posn = ops_log.xview()
        ops_log.configure(state="normal")
        ops_log.delete("1.0","end")   
        ops_log.insert("1.0", UserScripts.ActiveSubprocesses.loggers[selection].getlog())
        ops_log.configure(state="disabled")
        
        if float(yscrollbar_posn[1]) == 1.0:
            # So that user can control scrollbar without its position resetting repeatedly        
            ops_log.yview_moveto(yscrollbar_posn[1]) 
        else:
            # So that scrollbar appears at bottom if not in use
            ops_log.yview_moveto(yscrollbar_posn[0])

        ops_log.xview_moveto(xscrollbar_posn[0])

    # Settings colours to scripts based on status
    if insert_listitems_func.finished == True:
        for key in UserScripts.statuses.keys():
            ops_treeview.item(key, tags = UserScripts.statuses[key])

    root.after(200, show_selected_log)




main_thread = threading.Thread(target = main)

process_log_extractor_thread = threading.Thread(target = process_log_extractor)

main_thread.start()


def mainloop_callback():
    if USER_CONSTANTS.SHOW_WINDOW is False:
        root.after(10, withdraw_window)
    root.after(500, show_selected_log)

root.protocol('WM_DELETE_WINDOW', withdraw_window)
root.after(10, mainloop_callback)
root.mainloop()
