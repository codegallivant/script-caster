import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
import os
import pyautogui as pag   
import ctypes
from ui.operations import *
from copy import deepcopy
# from classes import *


scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("exterior").sheet1
data = sheet.get_all_records()[0]

DEBUGMODE = data["DEBUGMODE"]

if DEBUGMODE=='True':
	print(data)

for col in range(1,len(data)+1):
	var=sheet.cell(1,col).value 	
	exec(f"{var} = data[var]")	
	exec(f'''
if {var}=="":
	{var}=None
elif {var}=="True":
	{var}=True
elif {var}=="False":
	{var}=False
else:
	#{var}=str(data[{var}])
	pass
'''
	)
	if DEBUGMODE=='True' or DEBUGMODE == True:
		print(f"{var}={data[var]}")

class Job:
	def __init__(self, code):
		self.code = code

	def execute(self):
		exec(self.code)


nodes = deepcopy(operations)
processes = deepcopy(operations)

for key in list(operations['non-uniform'].keys()):
	exec(f"nodes['non-uniform'][key] = {key}")
	processes['non-uniform'][key] = Job('')
	processes['non-uniform'][key].code=operations['non-uniform'][key]

def non_uniformers():
	for key in list(nodes['non-uniform'].keys()):
		if nodes['non-uniform'][key] is True:
			processes['non-uniform'][key].execute()

if SWITCH == True:
	non_uniformers()

'''	if __name__ == '__main__':
		for key in functions.keys() :
		#freeze_support()
			if {key}==True and key is not 'SWITCH':
				functions[key] = Process(target= functions[key].execute)
				functions[key].start()'''

'''if DEBUGMODE==False:


if SWITCH==False:
	JobMaker('uniform','SWITCH')

if DESKRIGHT==True:
	pag.hotkey("ctrl","winleft","right")
elif DESKLEFT==True:
	pag.hotkey("ctrl","winleft","left")
else:
	pass

if CODEXEC==True:
	try:
		exec(CODE)
		sheet.update_cell(2,18,"Success")
		print("Code Execution was Successful!")
	except:
		sheet.update_cell(2,18,"Failure")
		print("Code Execution Failed! Please check the Code again and Retry.")

if SCREENLOG == True:
	image = pag.screenshot() 
	image.save("screenlog.jpg")
	with open('screenlog.jpg', mode='rb') as file:
	   img = file.read()
	sheet.update_cell(4,1,img)
'''




#if OPENCLICKER==True:
'''	p = Popen('clicker.exe', stdin=PIPE) #NOTE: no shell=True here
	p.communicate(os.linesep.join([MODE, X,Y, TIMELIMIT]))

	p = Popen(["clicker.exe"], stdin=PIPE, stdout=PIPE, bufsize=1)
	print p.stdout.readline(), # read the first line
	for i in range(10): # repeat several times to show that it works
	    print >>p.stdin, i # write input
	    p.stdin.flush() # not necessary in this case
	    print p.stdout.readline(), # read output

	print p.communicate("n\n")[0], # signal the child to exit,
	                               # read the rest of the output, 
	                               # wait for the child to exit
	                               '''


'''
if SCREENLOG==True:
	# take screenshot using pyautogui 
	image = pag.screenshot() 
	sheet.append_row(['image1', '=IMAGE(\"{image}\")'])

	
	# since the pyautogui takes as a  
	# PIL(pillow) and in RGB we need to  
	# convert it to numpy array and BGR  
	# so we can write it to the disk 
	#image = cv2.cvtColor(numpy.array(image), 
	 #                    cv2.COLOR_RGB2BGR) 
	   
	# writing it to the disk using opencv 
	
	#img = os.path.abspath(image)

	"""data = {}
				with open('some.jpg', mode='rb') as file:
				    img = file.read()"""


item = {}

data['img'] = base64.b64encode(img)
print(json.dumps(data))
	item = {}
	#data['img'] = base64.encodebytes(img).decode("utf-8")
	item['img'] = image
	#base64.encodebytes(image).decode("utf-8")
	print(json.dumps(item))

	"""folium.raster_layers.ImageOverlay(
				                     img,
				                     [[ya.min(), xa.min()], [ya.max(), xa.max()]],
				                     opacity=0.5).add_to(mapa)"""
	sheet.update_cell(4, 1, item)
	
'''


""""""
#! /usr/bin/env python
#import subprocess
#call(["node", "C:/Users/rekhasha/OneDrive - AMDOCS/Backup Folders/Desktop/Janak_HTML_Programs/connector.js"]) 
#subprocess.call('node connector.js', shell=True )
"""
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() 
# client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)
"""
# View all folders and file in your Google Drive
"""fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "To Share"):
      fileID = file['id']"""
"""
"""
# Initialize GoogleDriveFile instance with file id.
"""
file1 = drive.CreateFile({"mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
file1.SetContentFile("small_file.csv")
file1.Upload() # Upload the file.
print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))"""
"""

"""
#file_list = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()
"""
fileList = drive.ListFile({'q': "'1jXmM8DmF_Irz25EpXnf2PpRN4bM3Gv9u' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
   # Get the folder ID that you want
  if(file['title'] == "picture"):
      fileID = file['id']

"""
# Initialize GoogleDriveFile instance with file id.
"""
file2 = drive.CreateFile({'id': fileID})
file2.Trash()  # Move file to trash.
file2.UnTrash()  # Move file out of trash.
file2.Delete()  # Permanently delete the file.
"""
"""
"""


