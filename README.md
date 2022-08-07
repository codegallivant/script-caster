# script-caster

## Readme incomplete

<br><br>

###### BRIEF SUMMARY OF PROJECT:
This is a python application that enables a user to remotely execute user-scripts on their computer.
###### COMPLETION STATUS: 
*Under Development. Stable beta version complete.*

<br>

## Prerequisites:
- Python 3+
- pip modules (See `requirements.txt` for list of modules)
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
Also see [Google APIs Terms of Service](https://developers.google.com/terms).

<br>

### 2. Setting up Exterior (Online Google spreadsheet)
This is essentially a Google Sheets document i.e. a spreadsheet. It acts as a controller containing several parameters used to control the target computer remotely. 
To set it up, create a Google Sheets document identical to this [copy of my version of Exterior](https://docs.google.com/spreadsheets/d/1wjEeu2_Jghxce32vzDpUoDYcjO-0N8ttbz5VEFvCqRI/edit?usp=sharing) inside the google drive folder named Exterior.

<br>

### 3. Setting up a GitHub repository for your scripts
- This repository is for storing the user-scripts which you can create and run remotely.
- Currently only python scripts can be run
- Steps for creating user-scripts:
  1. Create a GitHub repository. 
  2. Create the script inside this repository.
  3. Create a switch for this script in Exterior.
- [Sample user-scripts](https://github.com/codegallivant/sample-scriptcaster-userscripts/)

<br>

### 4. Installing pip modules
Download the repository. From the command line, run this in the app's root directory - 
```
pip install -r requirements.txt
```

<br>

### 5. Running the application
**To run script-caster from the command line, execute the following code from the app root directory -**
```
pythonw main.pyw
```
Alternatively, you can just click on the file and open it with Python.

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
  - Specify the interval(in integer seconds) between each fetch request to the spreadsheet
  - **IMPORTANT:** Specifying a very low interval and continuously communicating with the program via Google API can be dangerous. See Google API [usage limits](https://developers.google.com/sheets/api/limits). Minimum interval time recommended is 5 seconds.
- `UPDATE_LOCAL_USER_SCRIPTS`
  - Input accepted
  - Checkmark this parameter if you've just changed user-scripts in your repo and want the changes to be downloaded locally. They will only be considered by the program after you've marked this parameter.
  
### User-Script parameters
- These parameters are used to manage the functioning of user-scripts. 
- To create a switch parameter, set the value of a cell to the user-script's name. In the cell below this one, you can set it to `ON` or `OFF`. Use of conditional formatting and data validation is recommended.
- To see the status for the execution of the user-script, in the same row as the switch parameter, do as follows - Set the value of a cell to `STATUS`. In the cell below this one, the program will automatically set the value as one of the following depending on the script's result - `Running`, `Done`, `Failed`, along with the timestamp.
- In your scripts, you can also make contact with Exterior and fetch/update values. To know more, see [gspread documentation](https://docs.gspread.org/en/latest/)

### Comments
To add a comment that will not be parsed by the program, set the value of a cell to `COMMENT`. In the cell below this one, you can set the comment. 

<br>

**See examples of user-script parameters and comments [here](https://docs.google.com/spreadsheets/d/1wjEeu2_Jghxce32vzDpUoDYcjO-0N8ttbz5VEFvCqRI/edit?usp=sharing)**
<br>
**NOTE:** When creating parameters, ensure headings of one parameter do not lie in the same row as values of another parameter. If you do this, the program may extract values incorrectly or throw an error.

<br>
<br>

## Other important files:

These files may be useful while creating user-scripts. 

#### 1. `ggl_api/exterior_connection.py`
`ggl_api/connection.py` holds functions that help establishing connection with the Exterior spreadsheet as well as updating its values easily. The functions are made such that the number of API requests sent is lesser than otherwise.

#### 2. `ggl_api/gdprocesses.py`
`ggl_api/gdprocesses.py` holds functions that help easily upload/download files or folders to/from Google Drive.

<br>
<br>

## Note
 
- This program is supposed to be able to run on all operating systems, though it has only been tested on Windows.
- user-scripts can only be executed on a target computer only if the application has been installed into the target computer.
- Program can only run on the target while the target computer while the target is awake.
- Program will only be able to fetch data and execute accordingly if it has access to the Internet.
- This is not meant as a hacking tool, nor does it suit one.
- [Icon(`favicon.ico`) credits: www.flaticon.com](https://www.flaticon.com/premium-icon/cloud-service_3211343?term=cloud&page=1&position=1&page=1&position=1&related_id=3211343&origin=search)
