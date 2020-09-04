import gprocesses
from gprocesses import get_id
import os


operations = {
	"uniform": {

	},
	"non-uniform": {

	}
}

def get_uniform_tasks():
	os.rmdir('C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out\\Outer_Core\\Uniform')
	gprocesses.download_folder("Exterior/Outer_Core/Uniform", "C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out", files_only = False)
	uniform_ops = gprocesses.get_list(get_id('Exterior/Outer_Core/Uniform'))
	for op in uniform_ops:
		operations['uniform'][op['title']]=f'''
import Outer_Core.Uniform.{op['title']} as {op['title']}
{op['title']}.main()
'''

def get non_uniform tasks():
	os.rmdir('C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out\\Outer_Core\\Non_Uniform')
	gprocesses.download_folder("Exterior/Outer_Core/Non_Uniform", "C:\\Users\\rekhasha\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\Janak_HTML_Programs\\mental_out", files_only = False)
	non_uniform_ops = gprocesses.get_list(get_id('Exterior/Outer_Core/Uniform'))
	for op in non_uniform_ops:
		operations['non-uniform'][op['title']]=f'''
import Outer_Core.Non_Uniform.{op['title']} as {op['title']}
{op['title']}.main()
'''


get_tasks()

