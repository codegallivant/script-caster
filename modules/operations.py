#THE OPERATIONS DICTIONARY DATASET:

operations = {


#UNIFORM Operations Start Here:

	"uniform" : {


		"SWITCH": {
			
			"True": """

print("Non-Uniform Operations Gateway is OPEN. Initiating Process...")
protect_connection('''
conexec.main()
''')
print("Process has ended. Instructions Executed.")
Exterior.SWITCH=False
protect_connection('''sheet.update_cell(2,1,"False")''')
print("Non-Uniform Operations Gateway has been CLOSED.")
		
			""",

			"False": """"""

		},

		"DEBUGMODE":{

			"True": """

global hidden
global the_program_to_hide

if hidden != False:
	print('Showing window...')
	win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)
	hidden = False


			""",
			"False":"""

global hidden
global the_program_to_hide

if hidden != True:
	print('Hiding window...')
	win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
	hidden = True

			"""
		},

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
	protect_connection('''sheet.update_cell(2,6,"Success")''')
	print("Code Execution was Successful!")
except:
	protect_connection('''sheet.update_cell(2,6,"Failure")''')
	print("Code Execution gave an exception! Please check the code again and retry.")

Exterior.CODEXEC=False
protect_connection('''sheet.update_cell(2,4,"False")''')
print("Code Execution Gateway has been CLOSED.")

			""",

			"False": """"""
		}

	},


#NON-UNIFORM Operations Start Here:

	"non-uniform" : {

		"OPENCLICKER":"""
		""",
		"SCREENLOG" :"""

print("Taking screenshot...")
im1 = pag.screenshot()
im_name = "SCREEN_LOG " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S') + " .jpg"
print(f"'{im_name}' created")
im1.save(rf"C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out\\Screen_Logs\\{im_name}")
print(f"Uploading '{im_name}' to Exterior...")
# try:
gprocesses.upload_file('Exterior/Screen_Logs',r"C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out\\Screen_Logs", im_name)
print("Screenshot successfully uploaded to Exterior/Screen_Logs")
# except:
# 	print("The file could not be uploaded to Exterior/Screen_Logs")

		""", 
		"DESKRIGHT":"""
print("Switching to next virtual desktop")
pag.hotkey("ctrl","winleft","right")
		""",
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