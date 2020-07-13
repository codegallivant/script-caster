#import os
#import hide
#import asyncio
#from subprocess import *
#from multiprocessing import Process
#import sys
#import time
#import datetime

class Job:
	def __init__(self, code):
		self.code = code

	def execute(self):
		exec(self.code)