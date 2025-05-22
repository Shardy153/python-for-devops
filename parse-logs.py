### Log File Analyzer

#Problem*: Parse a log file and count occurrences of each HTTP status code (e.g., 200, 404).
#Skills: File I/O, Dictionaries, String Parsing

import os

current_dir = os.getcwd()
# print(f"Current Directory: {current_dir}")

log_file = os.path.join(current_dir, 'log.txt')

print(f"Log File Path: {log_file}")

d = {}

with open(log_file, 'r') as f:
    for line in f: 
    	l = line.strip().split()
    	d[l[-2]] = d.get(l[-2], 0) + 1

print(d)    	
