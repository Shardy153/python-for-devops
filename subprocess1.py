# Docker Container Lister
# Goal: List all running Docker containers using subprocess.
# Extract container ID, name, and status.


import subprocess
import re
from prettytable import PrettyTable


output = subprocess.run(["docker ps -a"], capture_output=True, shell=True)
output = output.stdout.decode("utf-8")
lines = output.splitlines()
words = re.split(r'\s{2,}', lines[0])	
t = PrettyTable([words[1],words[4], words[-1]])


for line in lines[1:]:
	words = re.split(r'\s{2,}', line)	
	t.add_row([words[1],words[4], words[-1]])


print(t)
