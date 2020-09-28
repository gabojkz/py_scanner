#!/usr/bin/env python3
import sys
import os
import getpass
import subprocess
import asyncio

run  = True
def message():
	filename = 'help.txt'
	try: 
		with open(filename) as file:
			return file.read()
	except:
		print('Error laoding help.txt file')

def get_root():
	try: 
		machine_user =  getpass.getuser()
	except:
		print('Fatal Error this machine does not have a user.')	
		return False
	
	print('\nMachine name: {}'.format(machine_user))

	root = '/Users/{machine_user}'.format_map({'machine_user': machine_user})
	return root

def get_args():
	args = sys.argv
	def_path = get_root()

	if len(args) <= 1:
		print( '\n'
				'No arguments provided \n'
				'Will use default args ...')
	else:
		def_path = args[1]

	print("Dir: {}".format(def_path))

	return def_path

if __name__ == '__main__':
	print(message())
	path = get_args()

	cmd = 'du -ahx {path} | sort -rh | head -5'.format_map({'path': path})

	print('\nStarting scanning ...\n')
	output = subprocess.Popen(cmd,  
		shell=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)

	stdout, stderr = output.communicate()

	for line in stdout.splitlines():
		print(line.decode('UTF-8'))

