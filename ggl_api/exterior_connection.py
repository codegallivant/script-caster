import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authenticate():
#	print("Connecting to Google Spreadsheets...")
	scope = ['https://spreadsheets.google.com/feeds',
	'https://www.googleapis.com/auth/drive']
#	print("Authenticating...")
	creds = ServiceAccountCredentials.from_json_keyfile_name('creds/service_account_credentials.json', scope)
	client = gspread.authorize(creds)
#	print("Authentication Successful!")
	return client


def open_sheet(file_name, sheet_name, client):
	sheet = client.open(file_name).worksheet(sheet_name)
	return sheet


def update_parameter_cell_value(sheet, parameter_name, new_cell_value, value_type="status"):
	if value_type == "status":
		sheet.update_cell(sheet.find(parameter_name).row+1,sheet.find(parameter_name).col, new_cell_value)
	elif value_type == "result":
		sheet.update_cell(sheet.find(parameter_name).row+2,sheet.find(parameter_name).col, new_cell_value)