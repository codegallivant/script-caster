import gspread
from oauth2client.service_account import ServiceAccountCredentials
from copy import deepcopy
import datetime
import time


def authenticate(creds_path):
#	print("Connecting to Google Spreadsheets...")
	scope = ['https://spreadsheets.google.com/feeds',
	'https://www.googleapis.com/auth/drive']
#	print("Authenticating...")
	creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
	client = gspread.authorize(creds)
#	print("Authentication Successful!")
	return client


def open_sheet(file_name, sheet_name, client):
	sheet = client.open(file_name).worksheet(sheet_name)
	return sheet


def find_parameter_cells(sheet, parameter_name, subparameter_name=None, sheet_values=None):
	
	if sheet_values == None:
		sheet_values = sheet.get_all_values()
	
	parameter_found = False
	subparameter_found = False
	
	value_row = None
	value_col = None
	subparameter_row = None
	subparameter_col = None

	if subparameter_name == None: # So that function returns parameter value if no subparameter is specified
		subparameter_name = parameter_name
	
	for row in sheet_values:
		for cell in row:
			if cell==parameter_name:
				value_row = sheet_values.index(row)+1
				value_col = row.index(cell)+1
				parameter_found = True
			if cell==subparameter_name:
				subparameter_row = sheet_values.index(row)+1
				subparameter_col = row.index(cell)+1
				subparameter_found = True
		if parameter_found == True and subparameter_found == True:
			if subparameter_row == value_row:
				break	
	
	return [subparameter_row,subparameter_col]


def update_parameter_value(sheet, parameter_name, new_cell_value, sheet_values=None):
	cell = find_parameter_cells(sheet, parameter_name, None, sheet_values)
	sheet.update_cell(cell[0]+1, cell[1], new_cell_value)

def update_parameter_status(sheet, parameter_name, new_cell_value, sheet_values=None):
	cell = find_parameter_cells(sheet, parameter_name, "STATUS", sheet_values)
	sheet.update_cell(cell[0]+1, cell[1], new_cell_value)


def get_parameter_values(sheet=None, sheet_values=None):
	# Returns a dict where parameter: value below it
	result_dict = dict()
	if sheet == None and sheet_values == None:
		return
	if sheet == None:
		values = deepcopy(sheet_values)
	if sheet_values == None:
		values = sheet.get_all_values() #Returns list of lists where [[r1c1,r1c2,r1c3...],[r2c1,r2c2,r2c3...],...]
	# print(values)
	values_copy = deepcopy(values)
	# print(values)

	skip_next_row = False
	for row in values:
		if skip_next_row == True: 
			skip_next_row = False
			continue #Skipping row because its filled with values not headers
		
		# Following code is executed after confirming above that row is header row
		
		
		for cell in row:
			if cell == 'COMMENT' or cell == 'STATUS':
				values[values.index(row)+1][row.index(cell)]=''
				values[values.index(row)][row.index(cell)]=''


		for cell in values[values.index(row)]:
			# print(row)
			# print(cell)
			# print()
			if cell == '':
				continue					
			result_dict[cell] = values[values.index(row)+1][row.index(cell)]
			# print(result_dict)
			# print()
			# print(values)
			# print()
			skip_next_row = True

	return [values_copy, result_dict]


# code for testing - 
# client = authenticate('service_account_credentials.json')
# sheet = open_sheet("Exterior","SYSTEM_0", client)
# all_sheet_values,x = get_parameter_values(sheet)
# update_parameter_value(sheet,'LAST_CONTACT_TIME', datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%Y %H:%M:%S'), all_sheet_values)