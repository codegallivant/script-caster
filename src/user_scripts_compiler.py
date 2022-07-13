import os
from github import Github 


# def get_formatted_scripts_str_dict(repo):
#     s=""
#     s+="user_scripts = {"
#     # for i in range(1,3):
#         # if i == 1:
#         #     op_type = "UNIFORM"
#         # elif i==2:
#         #     op_type = "NON-UNIFORM"
#     # contents = repo.get_contents(op_type)
#     contents = repo.get_contents("")
#     # s+="\n\t\'"+op_type+"\': {\n\n"
#     while len(contents)>0:
#         file_content = contents.pop(0)
#         # s+="\n\t'"+os.path.splitext(file_content.name)[0]+"' : " + "\"\"\"\n"+file_content.decoded_content.decode('utf-8')+"\n\"\"\","
#         s+="\n\t'" + os.path.splitext(file_content.name)[0] + "' : '',"
#     s+="\n}"
#     return s


def update_scripts(access_token, username, ops_repo_name, path):
    g = Github(access_token)
    repo = g.get_repo(f"{username}/{ops_repo_name}")
    contents = repo.get_contents("")
    user_scripts_list = []
    # ops_file = open(f"{path}/user_scripts_dict.py",'w')
    # ops_file.write(get_formatted_scripts_str_dict(repo))
    # ops_file.close()
    while len(contents) > 0:
        file_content = contents.pop(0)
        user_scripts_list.append(os.path.splitext(file_content.name)[0])
        ops_file = open(f"{path}/user_script_files/{os.path.splitext(file_content.name)[0]}.py",'w')
        ops_file.write(file_content.decoded_content.decode('utf-8'))
        ops_file.close()
    return user_scripts_list


# def get_scripts_dict():
#     import user_scripts.user_scripts_dict as user_scripts_dict
#     return user_scripts_dict.user_scripts


