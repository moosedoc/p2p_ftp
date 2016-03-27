# project imports
import os

def get_file(self, file=None):
	exists = os.path.exists(file)
	if exists:
		return file
	else: 
		-1
