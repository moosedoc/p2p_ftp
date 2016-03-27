# project imports
import os

def check_file(file=[]):
	# check if file exists
	for f in file:
		exists = os.path.exists(file)
		# return if true, else return -1
		if exists:
			return file
		else: 
			return -1

def delete_file(file=[]):
	return 

def get_file(file=[]):
	return
