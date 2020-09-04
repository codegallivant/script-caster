from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import os 


class client:
	pass


def authenticate_client():

	client.gauth = GoogleAuth()
	gauth=client.gauth

	# Try to load saved client credentials
	gauth.LoadCredentialsFile("mycreds.txt")

	if gauth.credentials is None:
	    # Authenticate if they're not there
	    gauth.GetFlow()
	    gauth.flow.params.update({'access_type': 'offline'})
	    gauth.flow.params.update({'approval_prompt': 'force'})
	    gauth.LocalWebserverAuth()
	elif gauth.access_token_expired:
	    # Refresh them if expired
	    gauth.Refresh()
	else:
	    # Initialize the saved creds
	    gauth.Authorize()

	# Save the current credentials to a file
	gauth.SaveCredentialsFile("mycreds.txt")  
	client.drive = GoogleDrive(client.gauth)


def list_files(folder_id):

	authenticate_client()

	return client.drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()


def get_id(folder_path):

	fileID = None

	try:

		folder_path = folder_path.split('/')

		fileList = client.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

		for file in fileList:
			if file['title']==folder_path[0]:
				fileID = file['id']
				break
		folder_path.pop(0)

		for folder_name in folder_path:
			fileList = client.drive.ListFile({'q': f"'{fileID}' in parents and trashed=false"}).GetList()
			for file in fileList:
				if file['title']==folder_name:
					fileID = file['id']
					break

	except:

		fileID = False

	finally:

		return fileID


def upload_file(target_folder_path , home_path, file_name):

	authenticate_client()

	target_id = get_id(target_folder_path)
	if target_id == False:
		print(f"[ ERROR in gprocesses.py ] : {target_folder_path} not found.")
		return False
	home_path = rf"{home_path}"

	f = client.drive.CreateFile({
		'title': file_name, 
		'parents': [{'id': target_id}]
		}) 
	f.SetContentFile(os.path.join(home_path, file_name)) 
	f.Upload()


def download_file(target_file_path, home_path):

	authenticate_client()

	target_id = get_id(target_file_path)
	if target_id == False:
		print(f"[ ERROR in gprocesses.py ] : {target_file_path} not found.")
		return False
	home_path = rf"{home_path}"

	file = client.drive.CreateFile({'id': target_id})
	working_path = os.getcwd()
	os.chdir(home_path)
	file.GetContentFile(file['title'])
	os.chdir(working_path)


# download_file("Exterior/Screen_Logs/SCREEN_LOG 2020-08-03 22-30-54 .jpg", "C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out\\TestDownloads")


def download_folder(target_folder_path, home_path, files_only = True):

	authenticate_client()
	
	working_path = os.getcwd()

	target_id = get_id(target_folder_path)

	if target_id == False:
		print(f"[ ERROR in gprocesses.py ] : {target_folder_path} not found.")
		return False
	home_path = rf"{home_path}"

	if files_only == False:
		home_path = os.path.join(home_path,target_folder_path.split('/')[len(target_folder_path.split('/'))-1])
		print(home_path)
		os.mkdir(home_path, 0o666)

	files=list_files(target_id)
	for file in files:
		file = client.drive.CreateFile({'id': file['id']})
		os.chdir(home_path)
		file.GetContentFile(file['title'])
		os.chdir(working_path)


# download_folder ("Exterior/Screen_Logs", "C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out\\TestDownloads")
