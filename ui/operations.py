operations = {

	"uniform" : {

		"SWITCH":"""
print("GATEWAY IS OPEN. Initiating Process...")
import conexec
print("Process has ended. Instructions Executed.")
refresh.SWITCH=False
sheet.update_cell(2,1,"False")
print("GATEWAY HAS BEEN CLOSED.")
		
		""",
		"DEBUGMODE":"""

global hidden
global the_program_to_hide

if hidden != True:
	if refresh.DEBUGMODE == False or refresh.DEBUGMODE == 'False':
		print('Hiding window...')
		win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
		hidden = True

if hidden != False:
	if refresh.DEBUGMODE == True or refresh.DEBUGMODE == 'True':
		print('Showing window...')
		win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)
		hidden = False

# kernel32 = ctypes.WinDLL('kernel32')
# user32 = ctypes.WinDLL('user32')
# SW_HIDE = 0
# hWnd = kernel32.GetConsoleWindow()
# user32.ShowWindow(hWnd, SW_HIDE)


		""",
		"STAYAWAKE":"""
pag.press('f15')
countdown(60, "STAYING AWAKE. Next Press:")
		""",
		"CLOSEALL":"""
		""",
		"CHECKINTERVAL":"""
		"""
	},

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
		""",
		"CODEXEC":"""
print('Recieved code will now be executed.')
try:
	exec(CODE)
	sheet.update_cell(2,18,"Success")
	print("Code Execution was Successful!")
except:
	sheet.update_cell(2,18,"Failure")
	print("Code Execution Failed! Please check the Code again and Retry.")
		"""

	}
}