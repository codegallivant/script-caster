import json
import os


default_data = {
	"COMPUTER_NAME": "",
	"PROJECT_PATH":os.path.dirname(os.path.abspath(__file__)),
	"SHOW_WINDOW":False,
	"MAX_LOG_LENGTH":10000,
	"GITHUB_USERNAME":"",
	"GITHUB_REPO_NAME":"",
	"GITHUB_ACCESS_TOKEN":""
}


def create():
	f = open("USER_CONSTANTS.json", 'w')
	f.seek(0)
	json.dump(default_data, f)
	f.truncate()
	f.close()


def is_created():
	return os.path.isfile("USER_CONSTANTS.json")


def is_modified():
	f = open("USER_CONSTANTS.json",'r')
	if get_dict() == default_data:
		f.close()
		return False
	else:
		f.close()
		return True


def get_dict():
	f = open("USER_CONSTANTS.json",'r')
	user_constants_dict = json.loads(f.read())
	f.close()
	return user_constants_dict


# def load():
#     user_constants_dict = get_dict()
    # for constant_name in user_constants_dict.keys():
    #     if user_constants_dict[constant_name] == "True" or user_constants_dict[constant_name]=="False" or user_constants_dict[constant_name]=="None":
    #         user_constants_dict[constant_name] = eval(user_constants_dict[constant_name])
#         exec(f"""
# global {constant_name}
# {constant_name} = user_constants_dict[constant_name]
# """)
    

def get(constant_name):
	data = get_dict()
	return data[constant_name]


def update(constant_name, new_constant_value):
    data = get_dict()
    f = open("USER_CONSTANTS.json", 'w')
    data[constant_name] = new_constant_value
    f.seek(0)  # rewind
    json.dump(data, f)
    f.truncate()
    f.close()
    # load()


# if is_created():
# 	load()

