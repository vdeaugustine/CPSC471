# *********************************************************************
# This file illustrates how to execute a command and get it's output
# *********************************************************************
import subprocess


def run_ls():
	# Run ls command, get output, and print it
	for line in subprocess.getstatusoutput('ls -l'):
		print(line)



def run_put():
	pass


def run_get():
	pass
