import json
import os


default_data = {
	"COMPUTER_NAME": "",
	"APP_FOLDER_PATH":os.path.dirname(os.path.abspath(__file__)),
	"USERSCRIPTS_FOLDER_PATH": os.path.join(os.path.dirname(os.path.abspath(__file__)),"local_user_scripts/"),
	"SHOW_WINDOW":False,
	"MAX_LOG_LENGTH":10000,
	"GITHUB_USERNAME":"",
	"GITHUB_REPO_NAME":"",
	"GITHUB_ACCESS_TOKEN":""
}


def create():
	f = open("USER_VARIABLES.json", 'w')
	f.seek(0)
	json.dump(default_data, f)
	f.truncate()
	f.close()


def is_created():
	return os.path.isfile("USER_VARIABLES.json")


def get_dict():
	f = open("USER_VARIABLES.json",'r')
	user_variables_dict = json.loads(f.read())
	f.close()
	return user_variables_dict


def is_modified(user_variable_name=None):
	user_variables_dict = get_dict()
	if user_variable_name == None: #Check all constants 
		modified = user_variables_dict != default_data
	else: # Check only specified constant
		modified = user_variables_dict[user_variable_name] != default_data[user_variable_name]  
	return modified


# def load():
#     user_variables_dict = get_dict()
    # for user_variable_name in user_variables_dict.keys():
    #     if user_variables_dict[user_variable_name] == "True" or user_variables_dict[user_variable_name]=="False" or user_variables_dict[user_variable_name]=="None":
    #         user_variables_dict[user_variable_name] = eval(user_variables_dict[user_variable_name])
#         exec(f"""
# global {user_variable_name}
# {user_variable_name} = user_variables_dict[user_variable_name]
# """)
    

def get(user_variable_name):
	data = get_dict()
	return data[user_variable_name]


def update(user_variable_name, new_variable_value):
    data = get_dict()
    f = open("USER_VARIABLES.json", 'w')
    data[user_variable_name] = new_variable_value
    f.seek(0)  # rewind
    json.dump(data, f)
    f.truncate()
    f.close()
    # load()


# if is_created():
# 	load()

