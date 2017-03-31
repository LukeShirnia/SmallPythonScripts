from sys import argv
import os

def find_pids(pid_to_find):
	       for pid in os.listdir('/proc'):
				try:
					process_path = '/proc/%s/exe' % (pid)
					process = os.readlink(process_path)
	        	                if pid.isdigit() and pid_to_find in process:
        	        	                print process, pid
				except:
					pass

if len(argv) == 1:
	print "Please enter a process name as an argument"
elif len(argv) == 2:
	script, pid = argv
	find_pids(pid)
else:
	print "Too many arguments"
