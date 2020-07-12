# mental-out

#### Essential Component of project (Not uploaded to github): [Link to a copy of my version of Exterior](https://docs.google.com/spreadsheets/d/1bAAT5t-o9ya-MbPMGvo6VJ6bYalg1MXsXRyc7rcrLJc/edit?usp=sharing)


###### BRIEF SUMMARY OF PROJECT:
This is an application built using python. Basically, it enables a computer to be controlled remotely via Google Drive.<br>
In the following documentation for this application, you will understand how this app works and how you can make changes to suit your own needs.
###### COMPLETION STATUS: 
*Under Development. Nearly Complete.*
###### *ALIASES:* 
- mental-out 
- project-exterior
- esper4
- TKNRTE12
- connectject

<br>

## Prerequisites:
- Python 3.8
- Pip
- Pip Modules:
  - gspread
  - oauth2client.service_account
  - time
  - pyautogui
  - threading
  - copy
  - pywin32
  - win32gui
  - ctypes
  - os
  - sys
- Google Account (For Google Drive)
- Google API Console Service Account
- *client_secret.json file* in root directory

<!--Downloading the executable(Not uploaded yet) will prevent you from making changes of your own. You will have to use the exact same version of the spreadsheet I used to make this app. However, if you download the executable, you will not need Python 3.8 or pip.-->

<br><br>

## How it works:

**Here's the HOT Stuff! I will explain to you all you need to know to understand the code, at least enough to make personalized changes.**

<br>

### Google API Console 
1. Go to [Google's API Console](https://console.developers.google.com/) and sign in to your google account
2. Create a project
3. Create a service account with credentials and download the client_secret.json file
4. Store the client_secret.json in your project root <br>
You're done with this step! Lets move on!

<br>

### Files that may matter to you during personalization:
- Exterior
- operations.py
- trigger.py
- conexec.py

<br>

#### 1. Exterior
This is essentially a google spreadsheet. It acts as a controller containing several parameters used to control the target remotely. <br>
[Link to a copy of my version of Exterior](https://docs.google.com/spreadsheets/d/1bAAT5t-o9ya-MbPMGvo6VJ6bYalg1MXsXRyc7rcrLJc/edit?usp=sharing)

##### Some Important Parameters of Exterior (Uniform Operations):
**Parameters values can be entered *'True' (ON)* or *'False' (OFF)*. Some parameters may be *text or numbers.***
- ###### SWITCH
  - If True, enables other non-uniform operations to be run. After execution of operations, *SWITCH* is turned to False automatically to stop repetitive execution.
  - If False, disables non-uniform operations from running.
- ###### CHECKINTERVAL
This specifies the time interval between which requests will be sent. Only integer values will be accepted, else exceptions(errors) will occur. <br>
**Minimum time period recommended is 2 seconds.** **IMPORTANT**: <br>
Following are rules regarding requests sent through the Google API Console. Since *CHECKINTERVAL* specifies the time interval between requests, these have to be looked into:
1. Maximum no. of requests allowed in a day per project is 50000. Therefore a minimum of 1.728 seconds should be allowed between each request, so that the program can run for 24 hours, continuously.
2. Maximum no. of requests per 100 secs is 100 for each project. 
3. A maximum of 10 requests can be made per second per user
- ###### DEBUGMODE
  - If False, hides console window and blocks unnecassary print commands.
  - If True, shows console window and allows print commands.
- ###### STAYAWAKE
  - If True, forces target computer to stay awake.
  - If False, does nothing.

<br>

##### *Working* Non-Uniform Parameters of Exterior:
- ###### DESKRIGHT
  - If True, moves to next virtual desktop
  - If False, does nothing
- ###### DESKLEFT
  - If True, moves to previous virtual desktop
  - If False, does nothing
- ###### CODEXEC
  - If True, executes given python code in target's terminal.
  - If False, does nothing.<br>
  - **Note**: Code to be executed is taken from the *CODE* parameter in Exterior. Whether the code execution was a success or not is written into the *LASTCODESTATUS* parameter.

<br>

#### 2. operations.py
Here, in operations.py you will be able to decide actions taken when you activate parameters in Exterior.
To understand these, you will first have to understand 2 kinds of operations.
  -  **Uniform Operations** <br>
These are tasks that take a long time to be executed. They may even go on forever.
For example, forcing a computer to stay awake, will imply that the *STAYAWAKE* operation has to be active as long as the parameter is marked True. 
Uniform operations are executed together. Their timespan makes it impossible to execute them one by one.
  -  **Non-Uniform Operations** <br>
These are tasks which take a relatively shorter time to execute. At least you could say, they don't take forever. 
It is not necassary to execute non-uniform operations altogether simulataneously, since they have a short timespan. Non-Uniform operations are executed one by one.

###### THE OPERATIONS DICTIONARY
That aside, operations.py contains a dictionary dataset called 'operations'. 'operations' consists of uniform and non-uniform subsets which then contain subsets of names of parameters. It is necassary that these names remain the same as the parameters in Exterior. All code wished to be executed for these parameters must be placed within its respective parameter subset in the operations dictionary.<br>
And that's it! That's all you need to do to create a new operation.

###### *Threading Practices*
To understand uniform operations and non-uniform operations thoroughly, threading practices should be understood:<br>
**RuntimeError**s may be generated if many threads of code are run at once. Therefore, **caution** should be exercised when creating uniform operations.

<br>

#### 3. trigger.py
trigger.py can be called the main file, or the activator of the entire program. trigger.py is responsible for executing uniform operations and calling conexec.py, which handles non-uniform operations.

#### 4. conexec.py
conexec.py handles non-uniform operations, as stated before. For testing purposes, conexec.py is separated from trigger.py. Hence, conexec.py can be run independently and execute non-uniform operations one by one.


