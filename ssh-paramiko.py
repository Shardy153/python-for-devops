import paramiko

def ssh_server(hostname, username, command):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=hostname, username=username)

	stdin, stdout, stderr = client.exec_command(command)
	print(stdout.readlines(), stderr.readlines())
	client.close()


hostname = input("Enter hostname : ")
username = input("Enter username : ")
command = input("Enter command to execute : ")
ssh_server(hostname, username, command)
