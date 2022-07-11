#THE user-scripts DICTIONARY DATASET:

user_scripts = {


#UNIFORM user-scripts Start Here:

	"UNIFORM" : {


		"SWITCH": {
			
			"True": """

print("Non-Uniform user-scripts Gateway is OPEN. Initiating Process...")
protect_connection('''
conexec.main()
''')
print("Process has ended. Instructions Executed.")
Exterior.records['SWITCH']=False
protect_connection('''sheet.update_cell(2,1,"False")''')
print("Non-Uniform user-scripts Gateway has been CLOSED.")
		
			""",

			"False": """"""

		},

# 		"DEBUGMODE":{

# 			"True": """

# global hidden
# global the_program_to_hide

# if hidden != False:
# 	print('Showing window...')
# 	win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)
# 	hidden = False


# 			""",
# 			"False":"""

# global hidden
# global the_program_to_hide

# if hidden != True:
# 	print('Hiding window...')
# 	win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
# 	hidden = True

# 			"""
# 		},

		"STAYAWAKE": {

			"True":"""

pag.press('f15')
countdown(60, "Staying awake. Next F15 keypress:",logger=STAYAWAKElogger)

			""",

			"False":""""""

		},

		# "CHECKINTERVAL": {

		# 	"True":"""""",
		# 	"False":""""""

		# },

		"CODEXEC": {

			"True": """

print("Code Execution Gateway is OPEN.")
print('Recieved code will now be executed.')
try:
	exec(f'''
{Exterior.CODE}
''')

	protect_connection('''sheet.update_cell(sheet.find("CODEXEC").row+1,sheet.find("CODEXEC").col+1,"Success")''')
	print("Code Execution was Successful!")
except:
	protect_connection('''sheet.update_cell(sheet.find("CODEXEC").row+1,sheet.find("CODEXEC").col+1,"Failure")''')
	print("Code Execution gave an exception! Please check the code again and retry.")

Exterior.CODEXEC=False
protect_connection('''sheet.update_cell(sheet.find("CODEXEC").row+1,sheet.find("CODEXEC").col,"False")''')
print("Code Execution Gateway has been CLOSED.")

			""",

			"False": """
			"""
		}
	},


#NON-UNIFORM user-scripts Start Here:

	"NON-UNIFORM" : {
# 		"AUTOSAVESHOT": """

# def saveshot(): 
# 	print("Taking screenshot...")
# 	im1 = pag.screenshot()
# 	im_name = "Screenshot " + USER_CONSTANTS.COMPUTER_NAME + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S') + " .jpg"
# 	path = f"{USER_CONSTANTS.PROJECT_PATH}/Screen_Logs"
# 	im1.save(rf"{path}/{im_name}")
# 	print(f"'{im_name}' created.")
# 	print(f"Uploading '{im_name}' to Exterior...")
# 	protect_connection(f"gdprocesses.upload_file('Exterior/Screen_Logs/PrntScrn','{path}', '{im_name}')")
# 	# protect_connection(f"print({path})")
# 	print("Screenshot successfully uploaded to Exterior/Screen_Logs/PrntScrn .")

# print("Adding hotkey for print_screen...")
# keyboard.add_hotkey('print_screen', saveshot)
# print("Hotkey for print_screen added.")

# 			""",
		"BLOCKINPUT": """
print("Blockinput mecha started.")
ok = ctypes.windll.user32.BlockInput(True)
print("User Input Blocked. To enable, use Exterior.")
			""",
		"ALLOWINPUT": """
ok = ctypes.windll.user32.BlockInput(False)
print("User Input Unblocked.")
			""",
		"SCREENLOG" :"""

print("Taking screenshot...")
im1 = pag.screenshot()
im_name = "SCREEN_LOG " + USER_CONSTANTS.COMPUTER_NAME + " " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S') + " .jpg"

path = f"{USER_CONSTANTS.PROJECT_PATH}/user_scripts/user_script_generations/screen_logs"
im1.save(rf"{path}/{im_name}")
print(f"'{im_name}' created.")

print(f"Uploading '{im_name}' to Exterior...")
protect_connection("gdprocesses.authenticate_client('creds/mycreds.txt')")
protect_connection(f"gdprocesses.upload_file('Exterior/Screen_Logs','{path}', '{im_name}')")
print("Screenshot successfully uploaded to Exterior/Screen_Logs .")

		""", 
		"DESKRIGHT":"""
print("Switching to next virtual desktop")
pag.hotkey("ctrl","winleft","right")
		""" ,
 		"DESKLEFT":"""
print("Switching to previous virtual desktop")
pag.hotkey("ctrl","winleft","left")
 		"""
	}
}

# kernel32 = ctypes.WinDLL('kernel32')
# user32 = ctypes.WinDLL('user32')
# SW_HIDE = 0
# hWnd = kernel32.GetConsoleWindow()
# user32.ShowWindow(hWnd, SW_HIDE)