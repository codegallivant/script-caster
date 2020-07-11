
import ctypes

def hide(hidden):
	return '''
		kernel32 = ctypes.WinDLL('kernel32')
		user32 = ctypes.WinDLL('user32')
		SW_HIDE = 0
		hWnd = kernel32.GetConsoleWindow()
		user32.ShowWindow(hWnd, SW_HIDE)
		'''