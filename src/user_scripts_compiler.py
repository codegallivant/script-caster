import os
from github import Github 


def update_scripts(access_token, username, ops_repo_name, path):
    g = Github(access_token)
    repo = g.get_repo(f"{username}/{ops_repo_name}")
    contents = repo.get_contents("")
    user_scripts_list = []
    while len(contents) > 0:
        file_content = contents.pop(0)
        user_scripts_list.append(os.path.splitext(file_content.name)[0])
        ops_file = open(f"{path}/user_script_files/{os.path.splitext(file_content.name)[0]}.py",'w')
        ops_file.write(file_content.decoded_content.decode('utf-8'))
        ops_file.close()
    return user_scripts_list



