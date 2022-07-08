# mental-out

###### BRIEF SUMMARY OF PROJECT:
This is a python applications that enables a user to control their personal computer remotely via Google Drive. 
###### COMPLETION STATUS: 
*Under Development. Stable beta version complete.*

<br>

## Prerequisites:
- Python 3.8
- Pip
- Pip Modules:
  - sys
  - os
  - infi.systray
  - atexit
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
- Google Account
- Google API Console Service Account
- service_account_credentials.json file (For authenticating with Google API Console Service Account)

<br><br>

## Setting it up

<br>

### 1. Setting up your Google API Console Service Account
1. Go to [Google's API Console](https://console.developers.google.com/) and sign in to your google account
2. Create a project.
3. Create a service account integrated using the Google Sheets API and Google Drive API. Download the credentials as `service_account_credentials.json` file
4. Store the `service_account_credentials.json` file in your project root 
5. Done.

<br>

### 2. Setting up Exterior (Google Drive folder)
This is a Google Drive folder. This component of the project is helps in using `modules/gprocesses.py`, which helps in uploading files to and downloading files from your Google Drive. This is also required to use the non-uniform operation parameter `SCREENLOG` and `AUTOSAVESHOT`. This component cannot be downloaded from GitHub. To create it - 
1. Login to your Google account and go to Google Drive
2. Create a folder called `Exterior`
3. Add the Exterior spreadsheet in this folder
4. In order to be able to use the uniform operation parameter `SCREENLOG` and `AUTOSAVESHOT`, create folders named `Screen_Logs` and `PrntScrn` respectively inside this folder.

<br>

### 3. About Exterior (Online Google spreadsheet)
This is essentially a Google Sheets document i.e. a spreadsheet. It acts as a controller containing several parameters used to control the target computer remotely. 
To set it up, create a Google Sheets document identical to this [copy of my version of Exterior](https://docs.google.com/spreadsheets/d/11SisyrpYn2LrBczf60J63B3OrcTgtA3gbYHxtMuHZSA/edit?usp=sharing) inside the google drive folder named Exterior.

#### Parameters of Exterior
Parameter values can be entered - `True` (ON) or `False` (OFF). Some parameters may be text or numbers.


- ##### Uniform Operation Parameters 
  - `SWITCH`
    - If True, enables other non-uniform operations to be run. After execution of operations, `SWITCH` is turned to False automatically to stop repetitive execution.
    - If False, disables non-uniform operations from running.
  - `CHECKINTERVAL`
    - This specifies the time interval between which requests will be sent. Only integer values will be accepted, else exceptions(errors) will occur. <br>
    - **Minimum time period recommended is 2 seconds.** **IMPORTANT**: <br>
    - Following are rules regarding requests sent through the Google API Console. Since `CHECKINTERVAL` specifies the time interval between requests, these have to be looked into:
      1. Maximum no. of requests allowed in a day per project is 50000. Therefore a minimum of 1.728 seconds should be allowed between each request, so that the program can run for 24 hours, continuously.
      2. Maximum no. of requests per 100 secs is 100 for each project. 
      3. A maximum of 10 requests can be made per second per user
  - `STAYAWAKE`
    - If True, forces target computer to stay awake.
    - If False, does nothing.
  - `CODEXEC`
    - If True, executes given python code in target's terminal. After execution, automatically turns CODEXEC False to stop further repetitive execution.
    - If False, does nothing.<br>
    - **Note**: Code to be executed is taken from the `CODE` parameter in Exterior. Whether the code execution was a success or not is written into the `LASTCODESTATUS` parameter.

- ##### *Working* Non-Uniform Parameters:
  - `SCREENLOG`
    - If True, takes a screenshot and uploads it to Google Drive, in Exterior/Screen_Logs
    - If False, does nothing
  - `AUTOSAVESHOT`
    - If True, whenever you press PrntScrn on your keyboard, it takes a screenshot and uploads it to Google Drive, in Exterior/PrntScrn
    - If False, does nothing
  - `BLOCKINPUT`
    - If True, blocks all input device functioning
    - If False, does nothing
  - `ALLOWINPUT`
    - If True, unblocks all input device functioning
    - If False, does nothing
  - `DESKRIGHT`
    - If True, moves to next virtual desktop
    - If False, does nothing
  - `DESKLEFT`
    - If True, moves to previous virtual desktop
    - If False, does nothing

<br>

### 4. Setting up `USER_CONSTANTS.py`
```python
COMPUTER_CODE = 0 # Recommended to be a small positive integer. 
COMPUTER_NAME = "SYSTEM_" + str(COMPUTER_CODE) # Must match name of computer's respective sheet in Exterior.

PROJECT_PATH = "C:/.../mental_out" # Path of project root folder

DEBUG_MODE = False # Choose whether you want to see logs
```
0. Download the repository.
1. Create a file called `USER_CONSTANTS.py` in the modules folder.
2. Set values of `PROJECT_PATH` and `DEBUG_MODE`.
3. You may be using multiple computers with your Exterior spreadsheet. In order to differentiate them, assign each a different `COMPUTER_CODE` and create different sheets for each of them in the Exterior spreadsheet. When you set the name of their sheet in Exterior, ensure it matches with the respective  `COMPUTER_NAME`. In the example above, the sheet's name should be `SYSTEM_0`. 

<br>

### 5. Running the application
**To run mental-out from the command line, execute the following code from the project directory -**
```
python trigger.py
```
**Sidenote:** After the program starts, it automatically minimizes itself to the system tray. To see the console, right-click on the system tray icon and click `Show Console`. To quit the application, right-click on the icon in the system tray and click `Quit`.

<br>
<br>

## About other important files:
- `modules/operations.py`
- `trigger.py`
- `conexec.py`
- `common.py`
- `modules/connection.py`
- `modules/gprocesses.py`

### 1. `modules/operations.py`
Here, in `modules/operations.py` you will be able to decide actions taken when you activate parameters in Exterior.
To understand these, you will first have to understand 2 kinds of operations.
  -  **Uniform Operations** <br>
These are tasks that take a long time to be executed. They may even go on forever.
For example, forcing a computer to stay awake, will imply that the `STAYAWAKE` operation has to be active as long as the parameter is marked True. 
Uniform operations are executed together, at once, in separate threads. Their timespan makes it impractical to execute them one by one.
Creating too many simultaneous threads may result in delay in processing or even errors. Therefore, **caution** should be exercised when creating uniform operations.
  -  **Non-Uniform Operations** <br>
These are tasks which take a relatively shorter time to execute. At least you could say, they don't take forever. 
It is not necassary to execute non-uniform operations altogether simulataneously, since they have a short timespan. Therefore Non-Uniform operations are executed one by one.

#### THE OPERATIONS DICTIONARY
That aside, `modules/operations.py` contains a dictionary dataset called 'operations'. 'operations' consists of uniform and non-uniform subsets which then contain subsets of names of parameters. It is necassary that these names remain the same as the parameters in Exterior. All code wished to be executed for these parameters must be placed within its respective parameter subset in the operations dictionary.<br>
If you wish to execute it when the parameter is True, place it within the True subset of the parameter's subset. The same goes for False.
That's all you need to do to create a new operation.

<br>

### 2. `trigger.py`
**`trigger.py` can be called the main file, or the activator of the entire program.** `trigger.py` is responsible for executing uniform operations and calling `conexec.py`, which handles non-uniform operations.

<br>

### 3. `conexec.py`
`conexec.py` handles non-uniform operations, as stated before. For testing purposes, `conexec.py` is separated from `trigger.py`. Hence, `conexec.py` can be run independently and execute non-uniform operations one by one.

<br>

### 4. `common.py`
`common.py` imports modules for `trigger.py` and `conexec.py`. All modules to be imported (Be it pip or other) in these files must be imported through `common.py` .

<br>

### 5. `modules/connection.py`
`modules/connection.py` holds functions that help establishing connection with the Exterior spreadsheet.

<br>

### 6. `modules/gprocesses.py`
`modules/gprocesses.py` holds functions that help easily upload/download files or folders to/from Google Drive.

<br>
<br>

## Sidenotes

###### HANDLING INTERNET ISSUES
Engulf all code requiring internet connection within quotes as a parameter within the `protect_connection()` function to avoid crashing when internet issues arise.

###### CLARIFYING POTENTIAL MISCONCEPTIONS
- Actions can be conducted on a target computer only if the application has been installed into the target computer.
- It can only act on the target computer while the target is awake.
- It can only act on the target computer while the target has access to the internet. 
- This is not meant as a hacking tool, nor does it suit one. 
- This application has been built and tested on Windows 10 only, and will probably not work on any other OS.

