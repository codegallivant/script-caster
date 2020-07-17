#THE OPERATIONS DICTIONARY:

operations = {


#UNIFORM Operations Start Here:

	"uniform" : {


		"SWITCH": {
			
			"True": """

print("Non-Uniform Operations Gateway is OPEN. Initiating Process...")
from conexec import *
print("Process has ended. Instructions Executed.")
refresh.SWITCH=False
sheet.update_cell(2,1,"False")
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
countdown(60, "STAYING AWAKE. Next Press:",logger=STAYAWAKElogger)

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
{refresh.CODE}
''')
	sheet.update_cell(2,6,"Success")
	print("Code Execution was Successful!")
except:
	sheet.update_cell(2,6,"Failure")
	print("Code Execution gave an exception! Please check the code again and retry.")

refresh.CODEXEC=False
sheet.update_cell(2,4,"False")
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
		""", 
		"DESKRIGHT":"""
pag.hotkey("ctrl","winleft","right")
		""",
		"DESKLEFT":"""
pag.hotkey("ctrl","winleft","left")
		"""
	}
}

# if hidden != True:
# 	if refresh.DEBUGMODE == False or refresh.DEBUGMODE == 'False':
# 		print('Hiding window...')
# 		win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
# 		hidden = True

# if hidden != False:
# 	if refresh.DEBUGMODE == True or refresh.DEBUGMODE == 'True':
# 		print('Showing window...')
# 		win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)
# 		hidden = False

# kernel32 = ctypes.WinDLL('kernel32')
# user32 = ctypes.WinDLL('user32')
# SW_HIDE = 0
# hWnd = kernel32.GetConsoleWindow()
# user32.ShowWindow(hWnd, SW_HIDE)