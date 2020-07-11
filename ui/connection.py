import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect():
#	print("Connecting to Google Spreadsheets...")
	scope = ['https://spreadsheets.google.com/feeds',
	'https://www.googleapis.com/auth/drive']
#	print("Authenticating...")
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)
#	print("Authentication Successful!")
	return client

def opensheet(name, client):
	sheet = client.open(name).sheet1
	return sheet


