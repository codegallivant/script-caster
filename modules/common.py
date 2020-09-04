# Changing path at runtime
import sys
import json
import os
# targetpath = json.load(open('client_secret2.json',))
# targetpath = targetpath['project_path']
# sys.path.append(targetpath)
# sys.path.insert(0, os.path.abspath(targetpath))

#Pip Modules:
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
# import curses
# from classes import *
import pyautogui as pag
# from multiprocessing import Process
import threading
import win32
import win32gui
import win32.lib.win32con as win32con
import socket
import pyautogui as pag   
import ctypes
from copy import deepcopy
import datetime


# Operations Imports
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import modules.gprocesses as gprocesses

#Directory Imports
from modules.operations import *
from modules import connection as connection
# from classes import *

# Always import last:
import conexec
