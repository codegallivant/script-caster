from modules.common import *


client = connection.connect()
sheet = connection.opensheet('Exterior',socket.gethostname(),client)

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
	