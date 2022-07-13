import gspread
from oauth2client.service_account import ServiceAccountCredentials
from copy import deepcopy

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


def update_parameter_cell_value(sheet, parameter_name, new_cell_value, value_type="status", sheet_values=None):
	if sheet_values == None:
		sheet_values = sheet.get_all_values()
	# print(sheet_values)
	parameter_found = False
	result_found = False
	for row in sheet_values:
		for cell in row:
			if cell==parameter_name:
				cell_row = sheet_values.index(row)+1
				cell_col = row.index(cell)+1
				parameter_found = True
			if cell=="RESULT":
				result_row = sheet_values.index(row)+1
				result_col = row.index(cell)+1
				result_found = True
		if parameter_found == True and result_found == True:
			if result_row == cell_row:
				break	
	# print(result_row)
	# print(cell_row)
	if value_type == "status":
		sheet.update_cell(cell_row+1, cell_col, new_cell_value)
		# sheet.update_cell(sheet.find(parameter_name).row+1,sheet.find(parameter_name).col, new_cell_value)
	elif value_type == "result":
		sheet.update_cell(result_row+1, result_col, new_cell_value)
		# sheet.update_cell(sheet.find(parameter_name).row+1,sheet.find(parameter_name).col, new_cell_value)


def get_parameter_cell_values(sheet):
	# Returns a dict where parameter: value below it
	result_dict = dict()
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
			if cell == 'COMMENT' or cell == 'RESULT':
				values[values.index(row)+1][row.index(cell)]=''
				values[values.index(row)][row.index(cell)]=''

		
		# for cell in row:
		# 	if cell == '':
		# 		values[values.index(row)+1].pop(row.index(cell))
		# 		values[values.index(row)].pop(row.index(cell))

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


	