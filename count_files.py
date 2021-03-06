#!/usr/bin/python
# Author:       Luke Shirnia
# Source:       https://github.com/LukeShirnia/SmallPythonScripts/blob/master/count_files.py

from sys import argv
import sys
import os

def get_files_count(paths):
	files = folders = 0
	for _, dirnames, filenames in os.walk(paths):
		files += len(filenames)
		folders += len(dirnames)
	print paths
	#print "{:,} files, {:,} folders".format(files, folders)
	print "{0} files, {1} folders".format(files, folders)
	
if len(argv) == 1:
	print "Please enter a path to count"
if len(argv) == 2:
	script, path1 = argv 
	get_files_count(path1)
if len(argv) >= 3:
	print "Too many arguments"
