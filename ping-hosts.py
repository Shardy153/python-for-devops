### Ping Multiple Hosts
#Problem: Take a list of hostnames and use Python to ping each one, returning up/down status.
#Skills : `subprocess`, `os`, Error Handling

import subprocess

def ping_status(hostnames):
	response = {}
	for host in hostnames:
		ping_status = subprocess.run(["ping", "-c 2", host],capture_output=True, text=True)
		response[host] = "UP" if ping_status.returncode == 0 else "DOWN"
	return response	

print(ping_status(["127.0.0.1", "0.0.0.0", "8.8.8.8"]))
