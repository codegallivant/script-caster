import os
import shutil
from github import Github 


def update_scripts(access_token, username, repo_name, path):

    # Writing file contents from GitHub

    if access_token == None or access_token == "":
        g = Github()
    else:
        g = Github(access_token)

    repo = g.get_repo(f"{username}/{repo_name}")
    contents = repo.get_contents("")
    
    user_scripts_list = []
    
    while len(contents) > 0:
        file_content = contents.pop(0)
        # print(file_content.path)
        if file_content.type == "dir":
            os.mkdir(os.path.join(path, file_content.path))
            contents.extend(repo.get_contents(file_content.path))
        else:
            if os.path.splitext(file_content.name)[1].upper() == ".GITIGNORE":
                continue
            # split_filename = os.path.splitext(file_content.name)
            user_scripts_list.append(file_content.path)
            ops_file = open(os.path.join(path,file_content.path),'w')
            ops_file.write(file_content.decoded_content.decode('utf-8'))
            ops_file.close()
        
    return user_scripts_list



