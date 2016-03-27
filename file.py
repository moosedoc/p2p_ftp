# project imports
import os

def get_file(self, file=None):
	# check if file exists
	exists = os.path.exists(file)
	# return if true, else return -1
	if exists:
		return file
	else: 
		return -1
