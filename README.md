# script-caster

## Readme incomplete

<br><br>

###### BRIEF SUMMARY OF PROJECT:
This is a python application that enables a user to remotely execute user-scripts on their computer.
###### COMPLETION STATUS: 
*Under Development. Stable beta version complete.*

<br>

## Prerequisites:
- Windows OS (Due to usage of `pywin32` and `win32gui` pip modules)
- Python 3+
- Pip
- Pip Modules:
  - sys
  - os
  - pystray
  - gspread
  - oauth2client
  - pydrive
  - threading
  - win32
  - win32gui
  - ctypes
  - copy
  - datetime
  - keyboard
  - pyautogui
  - pillow
- Google Account
- Google API Console Service Account
- `creds/service_account_credentials.json` file (Credentials for Google Service Account)
- `creds/client_secret.json` file (Credentials for Google Drive API)
- GitHub Account 
- GitHub Personal Access Token (Only if using private repository to store user-scripts)

<br><br>

## Setting it up

<br>

### 1. Setting up your Google API Console Service Account
1. Go to [Google's API Console](https://console.developers.google.com/) and sign in to your google account
2. Create a project.
3. Create a service account integrated using the Google Sheets API and Google Drive API. 
4. Download the credentials as `service_account_credentials.json` file
5. Store the `service_account_credentials.json` file in the `creds/` folder. 
6. Done.

<br>

### 2. Setting up Exterior (Google Drive folder)
This is a Google Drive folder. This component of the project is helps in using `ggl_api/gdprocesses.py`, which helps in uploading files to and downloading files from your Google Drive. To create it - 
1. Login to your Google account and go to Google Drive
2. Create a folder called `Exterior`

<br>

### 3. Setting up Exterior (Online Google spreadsheet)
This is essentially a Google Sheets document i.e. a spreadsheet. It acts as a controller containing several parameters used to control the target computer remotely. 
To set it up, create a Google Sheets document identical to this [copy of my version of Exterior](https://docs.google.com/spreadsheets/d/1wjEeu2_Jghxce32vzDpUoDYcjO-0N8ttbz5VEFvCqRI/edit?usp=sharing) inside the google drive folder named Exterior.

<br>

### 4. Setting up a GitHub repository 
user-scripts can be stored in this repository. Only python files work.
If the repository is private, make sure to set up an access token in Settings > Developer Settings > Personal Access Token

<br>

### 4. Setting up `USER_CONSTANTS.py`
```python
COMPUTER_CODE = 0 # Recommended to be a small positive integer. 
COMPUTER_NAME = "SYSTEM_" + str(COMPUTER_CODE) # Must match name of computer's respective sheet in Exterior.

# Path of project folder
PROJECT_PATH = "C:/.../script-caster"

# Set defaults for displaying console/logs on program startup. Can also be changed after program starts by interacting with system tray icon.
DISPLAY_CONSOLE = True
SHOW_LOGS = True  # Recommended to be False if not viewing logs. Otherwise resources are used unnecessarily.

# GitHub Credentials
USERNAME = "<username_of_repo_holder>"  
OPS_REPO_NAME = "<repo_name>" 
ACCESS_TOKEN = "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" #For accessing private repos. Go to Developer Settings in Settings of your GitHub account to create a GitHub Personal Access Token. If you are using a public git repo, you can set ACCESS_TOKEN to None

```
0. Download the repository.
1. Create a file called `USER_CONSTANTS.py` in the root folder.
2. Set values of `PROJECT_PATH`, `DISPLAY_CONSOLE`, `SHOW_LOGS`, `USERNAME`, `OPS_REPO_NAME` and `ACCESS_TOKEN`. If you are using a public repo, you may set `ACCESS_TOKEN` to `None`.
3. You may be using multiple computers with your Exterior spreadsheet. In order to differentiate them, assign each a different `COMPUTER_CODE` and create different sheets for each of them in the Exterior spreadsheet. When you set the name of their sheet in Exterior, ensure it matches with the respective  `COMPUTER_NAME`. In the example above, the sheet's name should be `SYSTEM_0`. 

<br>

### 5. Running the application
**To run script-caster from the command line, execute the following code from the project root directory -**
```
python main.py
```
**Sidenote:** After the program starts, it creates an icon in the system tray. Upon right-clicking the system tray icon several options become visible.

<br>
<br>


## About Exterior (Google spreadsheet)
The program fetches data from Exterior every few seconds. Based on parameter values, it then executes user-scripts that it scrapes from GitHub.

### Hard-coded parameters
These parameters have been hard-coded into the main files of the program and are thoroughly involved in the code's execution.
- `CONTACT_STATUS`
  - Read only
  - Specifies whether program is able to access Exterior or not. 
  - The value of this parameter is related to other hard-coded parameters such as `LAST_CONTACT_TIME`, `CURRENT_TIME` and `TIME_DIFFERENCE`, which are also read-only.
- `REQUEST_INTERVAL`
  - Input accepted
  - Specifies interval(in integer seconds) between each fetch request to the spreadsheet
  - **IMPORTANT:** Specifying a very low interval and continuously communicating with the program via Google API can be dangerous. See Google API [usage limits](https://developers.google.com/sheets/api/limits).
- `UPDATE_LOCAL_USER_SCRIPTS`
  - Input accepted
  - Checkmark this parameter if you've just changed user-scripts in your repo and want the changes to be downloaded locally. They will only be considered by the program after you've marked this parameter.
  
### Other parameters
Yet to be written in readme


## Other important files:

These files may be useful while creating user-scripts. 

- `ggl_api/exterior_connection.py`
- `ggl_api/gdprocesses.py`

<br>

### 5. `ggl_api/exterior_connection.py`
`ggl_api/connection.py` holds functions that help establishing connection with the Exterior spreadsheet as well as updating its values easily.

<br>

### 6. `ggl_api/gdprocesses.py`
`ggl_api/gdprocesses.py` holds functions that help easily upload/download files or folders to/from Google Drive.

<br>
<br>

## Creating user-scripts
Yet to be added in readme

<br>
<br>

## Sidenotes
 
- This application has been built and tested on Windows 10 only. It cannot run on any other OS currently, due to the use of the modules `pywin32` and `win32gui` to hide the console. 
- user-scripts can only be executed on a target computer only if the application has been installed into the target computer.
- Program can only run on the target while the target computer while the target is awake.
- Program will only be able to fetch data and execute accordingly if it has access to the Internet.
- This is not meant as a hacking tool, nor does it suit one.
