from src.common import *


if not USER_CONSTANTS.is_created():
    USER_CONSTANTS.create()


os.chdir(USER_CONSTANTS.get("PROJECT_PATH"))


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



def set_defaults():

    # root.withdraw()
    set_defaults_window = tk.Toplevel(root)

    def on_closing():
        set_defaults_button["state"]="normal"
        set_defaults_window.destroy()
        # root.deiconify()

    set_defaults_window.protocol("WM_DELETE_WINDOW", on_closing)
    
    set_defaults_button["state"]="disabled"
    
    set_defaults_window.title("ScriptCaster - Settings")
    set_defaults_window.resizable(0,0)

    # set_defaults_window.geometry("780x800")

    # set_defaults_window_main_frame = tk.Frame(set_defaults_window)
    # set_defaults_window_main_frame.pack(fill="both", expand = True)
    # set_defaults_window_canvas = tk.Canvas(set_defaults_window_main_frame)
    # set_defaults_window_canvas.pack(side="left",fill="both",expand=True)
    # set_defaults_window_yscrollbar = tk.ttk.Scrollbar(set_defaults_window_main_frame,orient="vertical",command=set_defaults_window_canvas.yview)
    # set_defaults_window_yscrollbar.pack(side="right",fill="y")
    # set_defaults_window_canvas.configure(yscrollcommand=set_defaults_window_yscrollbar.set)
    # set_defaults_window_canvas.bind("<Configure>",lambda e: set_defaults_window_canvas.config(scrollregion= set_defaults_window_canvas.bbox("all"))) 
    # set_defaults_window_contents_frame = tk.Frame(set_defaults_window_canvas)
    # set_defaults_window_canvas.create_window((0,0),window= set_defaults_window_contents_frame, anchor="nw")

    set_defaults_window_contents_frame = tk.Frame(set_defaults_window)
    set_defaults_window_contents_frame.pack(ipady=10)

    input_frames = dict()
    input_labels =  dict()
    input_boxes = dict()
    user_constants_dict = USER_CONSTANTS.get_dict()

    input_frames["COMPUTER_NAME"] = tk.ttk.LabelFrame(set_defaults_window_contents_frame)
    input_frames["COMPUTER_NAME"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)

    input_frames["PROJECT_PATH"] = tk.ttk.LabelFrame(set_defaults_window_contents_frame)
    input_frames["PROJECT_PATH"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)
    
    input_frames["SHOW_WINDOW"] = tk.ttk.LabelFrame(set_defaults_window_contents_frame)
    input_frames["SHOW_WINDOW"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)
 
    input_github_frame = tk.ttk.LabelFrame(set_defaults_window_contents_frame, text = "GitHub Credentials")
    input_github_frame.pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)

    input_frames["GITHUB_USERNAME"] = tk.ttk.Frame(input_github_frame)
    input_frames["GITHUB_USERNAME"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)

    input_frames["GITHUB_REPO_NAME"] = tk.ttk.Frame(input_github_frame)
    input_frames["GITHUB_REPO_NAME"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)

    input_frames["GITHUB_ACCESS_TOKEN"] = tk.ttk.Frame(input_github_frame)
    input_frames["GITHUB_ACCESS_TOKEN"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)

    input_frames["MAX_LOG_LENGTH"] = tk.ttk.LabelFrame(set_defaults_window_contents_frame)
    input_frames["MAX_LOG_LENGTH"].pack(fill="x",padx = 25, pady = 5, ipady=5, ipadx=5)


    input_labels["COMPUTER_NAME"] = tk.ttk.Label(input_frames["COMPUTER_NAME"], text = "Enter the name of the sheet in Exterior that this computer must access.")
    input_labels["COMPUTER_NAME"].pack(anchor="w")
    input_boxes["COMPUTER_NAME"] = tk.ttk.Entry(input_frames["COMPUTER_NAME"], width=20)
    input_boxes["COMPUTER_NAME"].insert("end", user_constants_dict["COMPUTER_NAME"])
    input_boxes["COMPUTER_NAME"].pack(anchor="w", padx=10, pady=5)
    
    input_labels["PROJECT_PATH"] = tk.Label(input_frames["PROJECT_PATH"], text = "Enter the path of the app directory.")
    input_labels["PROJECT_PATH"].pack(anchor="w")
    input_boxes["PROJECT_PATH"] = tk.ttk.Entry(input_frames["PROJECT_PATH"], width=40)
    input_boxes["PROJECT_PATH"].insert("end", user_constants_dict["PROJECT_PATH"])
    input_boxes["PROJECT_PATH"].pack(anchor="w", side="left",padx=10, pady=5)

    def browsefunc():
        foldername =tk.filedialog.askdirectory()
        input_boxes["PROJECT_PATH"].insert("end", foldername) # add this

    input_project_path_browse_button = tk.ttk.Button(input_frames["PROJECT_PATH"],text="Browse",command=browsefunc)
    input_project_path_browse_button.pack(side="left")

    default_show_window_intvar = tk.IntVar(value=int(not USER_CONSTANTS.get("SHOW_WINDOW")))
    input_labels["SHOW_WINDOW"] = tk.Label(input_frames["SHOW_WINDOW"], text = "Minimize window to notification area (system tray) on app startup")
    input_boxes["SHOW_WINDOW"] = tk.ttk.Checkbutton(input_frames["SHOW_WINDOW"], variable  = default_show_window_intvar)
    input_boxes["SHOW_WINDOW"].pack(anchor="w", side="left",padx=10, pady=5)
    input_labels["SHOW_WINDOW"].pack(anchor="w", side="left")

    input_labels["MAX_LOG_LENGTH"] = tk.Label(input_frames["MAX_LOG_LENGTH"], text = "Set the maximum length of log lists. Upon exceeding this length, old logs will be deleted.")
    input_labels["MAX_LOG_LENGTH"].pack(anchor="w")
    input_boxes["MAX_LOG_LENGTH"] = tk.ttk.Entry(input_frames["MAX_LOG_LENGTH"], width=10)
    input_boxes["MAX_LOG_LENGTH"].insert("end", user_constants_dict["MAX_LOG_LENGTH"])
    input_boxes["MAX_LOG_LENGTH"].pack(anchor="w", padx=10, pady=5)

    input_labels["GITHUB_USERNAME"] = tk.Label(input_frames["GITHUB_USERNAME"], text = "Enter the username of the GitHub account containing your scripts.")
    input_labels["GITHUB_USERNAME"].pack(anchor="w")
    input_boxes["GITHUB_USERNAME"] = tk.ttk.Entry(input_frames["GITHUB_USERNAME"], width=25)
    input_boxes["GITHUB_USERNAME"].insert("end", user_constants_dict["GITHUB_USERNAME"])
    input_boxes["GITHUB_USERNAME"].pack(anchor="w", padx=10, pady=5)

    input_labels["GITHUB_REPO_NAME"] = tk.Label(input_frames["GITHUB_REPO_NAME"], text = "Enter the name of the GitHub repository containing your scripts.")
    input_labels["GITHUB_REPO_NAME"].pack(anchor="w")
    input_boxes["GITHUB_REPO_NAME"] = tk.ttk.Entry(input_frames["GITHUB_REPO_NAME"], width=25)
    input_boxes["GITHUB_REPO_NAME"].insert("end", user_constants_dict["GITHUB_REPO_NAME"])
    input_boxes["GITHUB_REPO_NAME"].pack(anchor="w", padx=10, pady=5)

    input_labels["GITHUB_ACCESS_TOKEN"] = tk.Label(input_frames["GITHUB_ACCESS_TOKEN"], text = "Enter your GitHub personal access token. If you are using a public repository, you may leave this field blank.")
    input_labels["GITHUB_ACCESS_TOKEN"].pack(anchor="w")
    input_boxes["GITHUB_ACCESS_TOKEN"] = tk.ttk.Entry(input_frames["GITHUB_ACCESS_TOKEN"], width=40, show="*")
    input_boxes["GITHUB_ACCESS_TOKEN"].insert("end", user_constants_dict["GITHUB_ACCESS_TOKEN"])
    input_boxes["GITHUB_ACCESS_TOKEN"].pack(anchor="w", padx=10, pady=5)


    def set_new_defaults():
        restart_required_list = ["PROJECT_PATH","COMPUTER_NAME","GITHUB_USERNAME", "GITHUB_REPO_NAME", "GITHUB_ACCESS_TOKEN"]
        restart_required = False
        for constant_name in user_constants_dict.keys():
            old_value = user_constants_dict[constant_name]
            if constant_name == "SHOW_WINDOW":
                value = not bool(default_show_window_intvar.get())
            elif constant_name == "MAX_LOG_LENGTH":
                value = int(input_boxes[constant_name].get())
            else:
                value = input_boxes[constant_name].get()
            if value != old_value and constant_name in restart_required_list:
                restart_required = True

            USER_CONSTANTS.update(constant_name, value)

        if restart_required == True:
            restart_program_fromTkWin()

        set_defaults_button["state"]="normal"
        set_defaults_window.destroy()
        # root.deiconify()


    update_defaults_warning_label = tk.Label(set_defaults_window_contents_frame, text = "If you change the app folder path, the sheet name, or your GitHub credentials, the app will restart.")
    update_defaults_warning_label.pack(anchor="w", pady=10, padx=15)


    back_set_defaults_button = tk.ttk.Button(set_defaults_window_contents_frame, text = "Back", command=on_closing)
    back_set_defaults_button.pack(side="left",anchor="w", pady=5, padx=20)

    update_defaults_button = tk.ttk.Button(set_defaults_window_contents_frame, text = "Update settings", command = set_new_defaults, style="Accent.TButton")
    update_defaults_button.pack(side="right",anchor="e", pady=5, padx=20)



top_section = tk.ttk.Frame(root)
top_section.grid(row=2,column=0, columnspan=2, sticky="ew", padx=15, pady=15, ipady=10)


# desc_section = tk.ttk.Frame(top_section)
# desc_section.pack(side="left",fill="x", expand = True, padx=15, ipady=10)

desc_section1 = tk.ttk.LabelFrame(top_section)
desc_section1.grid(row=1,column=1, sticky="w")
# desc_section1.grid(row=1,column=0,columnspan=2,sticky="ew")


set_defaults_button = tk.ttk.Button(top_section, text = "Settings", command = set_defaults, style="Accent.TButton")
set_defaults_button.grid(row=1,column=2, sticky="e", padx=(7,0))

desc_section2 = tk.ttk.LabelFrame(top_section)
# desc_section2.grid(row=2,column=0,columnspan=2,sticky="ew")
desc_section2.grid(row=2,column=1,columnspan=2, sticky="ew")


desc_text_strvar1 = tk.StringVar()
desc_text1 = tk.Label(desc_section1, textvariable = desc_text_strvar1, justify='left', wraplength=800, padx=5, pady=5, width=105, anchor="w")
desc_text1.pack(anchor="w")
desc_text_strvar2 = tk.StringVar()
desc_text2 = tk.Label(desc_section2, textvariable = desc_text_strvar2, justify='left', wraplength=800, padx=5, pady=5, width=105, anchor="w")
desc_text2.pack(anchor="w")

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
ops_log_section.grid(row=3,column=1, sticky='nsew', padx=15)

ops_log = tk.Text(ops_log_section, borderwidth=0)
ops_log.configure(state="disabled")
ops_log_section_xscrollbar = AutoScrollbar(ops_log_section, orient = "horizontal", command=ops_log.xview)
ops_log_section_yscrollbar = AutoScrollbar(ops_log_section, orient = "vertical", command=ops_log.yview)
ops_log.config(xscrollcommand=ops_log_section_xscrollbar.set, yscrollcommand=ops_log_section_yscrollbar.set)

ops_log.grid(row=1,column=1, sticky='nsew')
ops_log_section_xscrollbar.grid(row=2, column=1, sticky='ew')
ops_log_section_yscrollbar.grid(row=1,column=2, sticky='ns')


ops_treeview_section.grid_remove()
ops_log_section.grid_remove()
desc_section2.grid_remove()

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
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel) and widget.title() == "ScriptCaster - Settings":
            set_defaults_button["state"] = "normal"
            widget.destroy()
            break
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
footer_name_label = tk.Label(footer_section, text = f"{USER_CONSTANTS.get('COMPUTER_NAME')}", borderwidth=1, relief="solid", padx=2)
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
        max_len = USER_CONSTANTS.get("MAX_LOG_LENGTH")
        if max_len != None:
            if len(self.log)==max_len:
                self.log.pop(0)
            elif len(self.log)>max_len:
                self.log = self.log[len(self.log)-max_len+1:]
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
            mainlogger1.updatelog(f'{USER_CONSTANTS.get("COMPUTER_NAME")} is currently connected to Exterior/{USER_CONSTANTS.get("COMPUTER_NAME")}')
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



def update_local_user_scripts():
    user_scripts_names = user_scripts_compiler.update_scripts(USER_CONSTANTS.get("GITHUB_ACCESS_TOKEN"), USER_CONSTANTS.get("GITHUB_USERNAME"), USER_CONSTANTS.get("GITHUB_REPO_NAME"), f"{USER_CONSTANTS.get('PROJECT_PATH')}/local_user_scripts")
    user_scripts_statuses = dict()
    for user_script_name in user_scripts_names:
        user_scripts_statuses[user_script_name] = 'None'
    return  user_scripts_statuses



def main():
    
    main.initialized = False

    global mainlogger1
    global mainlogger2
    
    global sheet
    
    global process_log_extractor_thread

    mainlogger1.updatelog(f'Welcome {USER_CONSTANTS.get("COMPUTER_NAME")} !')

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
            sheet = exterior_connection.open_sheet('Exterior',USER_CONSTANTS.get("COMPUTER_NAME"), client)
            mainlogger1.updatelog(f"Connected with Exterior/{USER_CONSTANTS.get('COMPUTER_NAME')}")
            break
        except:
            countdown(60, f"Exterior/{USER_CONSTANTS.get('COMPUTER_NAME')} could not be opened. Next Attempt:", logger = mainlogger1)


    while True:
        try:
            mainlogger1.updatelog(f"Fetching user-scripts from GitHub/{USER_CONSTANTS.get('GITHUB_USERNAME')}/{USER_CONSTANTS.get('GITHUB_REPO_NAME')}...")
            UserScripts.statuses = update_local_user_scripts()
            mainlogger1.updatelog(f"Done.")
            break
        except:
            countdown(60, f"Failed to fetch user-scripts from GitHub/{USER_CONSTANTS.GITHUB_USERNAME}/{USER_CONSTANTS.GITHUB_REPO_NAME}. Next Attempt:", logger = mainlogger1)


    for key in UserScripts.statuses.keys():
        UserScripts.ActiveSubprocesses.loggers[key] = Logger('')

    
    main.initialized = True

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
                        new_env["PYTHONPATH"]=USER_CONSTANTS.get("PROJECT_PATH")
                        new_env["PYTHONUNBUFFERED"] = "1"
                        extension = os.path.splitext(key)[1]
                        if extension == '.py':
                            UserScripts.ActiveSubprocesses.processes[key] = subprocess.Popen(["python",f"{USER_CONSTANTS.get('PROJECT_PATH')}/local_user_scripts/user_script_files/{key}"], cwd = USER_CONSTANTS.get('PROJECT_PATH'), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, env=new_env)
                        elif extension == '.pyw':
                            UserScripts.ActiveSubprocesses.processes[key] = subprocess.Popen(["pythonw",f"{USER_CONSTANTS.get('PROJECT_PATH')}/local_user_scripts/user_script_files/{key}"], cwd = USER_CONSTANTS.get('PROJECT_PATH'), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, env=new_env)
                        
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

    if main.initialized == True:
        ops_treeview_section.grid()
        ops_log_section.grid()
        desc_section2.grid()
        main.initialized = None
    elif main.initialized == False:
        ops_treeview_section.grid_remove()
        ops_log_section.grid_remove()
        desc_section2.pack_forget()


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


    if list(ops_treeview.get_children()) != list(UserScripts.statuses.keys()):
        for item in ops_treeview.get_children():
            ops_treeview.delete(item)
        for user_script_name in UserScripts.statuses.keys():
            ops_treeview.insert('', index = "end",iid=user_script_name, values=(user_script_name))
    else:
        # Settings colours to scripts based on status
        for key in UserScripts.statuses.keys():
            ops_treeview.item(key, tags = UserScripts.statuses[key])

    root.after(200, show_selected_log)




main_thread = threading.Thread(target = main)

process_log_extractor_thread = threading.Thread(target = process_log_extractor)

main_thread.start()



def exit_handler():
    for process in UserScripts.ActiveSubprocesses.processes: 
        process.kill() 
 

atexit.register(exit_handler)




def mainloop_callback():
    if not USER_CONSTANTS.is_modified():
        set_defaults()
    else:
        if USER_CONSTANTS.get("SHOW_WINDOW") is False:
            root.after(10, withdraw_window)
    root.after(500, show_selected_log)


root.protocol('WM_DELETE_WINDOW', withdraw_window)
root.after(10, mainloop_callback)
root.mainloop()
