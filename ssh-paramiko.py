import paramiko

def ssh_server(hostname, username, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect without a password or key – consider adding password or key support if needed
    client.connect(hostname=hostname, username=username)
    
    stdin, stdout, stderr = client.exec_command(command)
    
    # Print stdout lines and stderr output
    print("Output:\n", ''.join(stdout.readlines()))
    print("Errors:\n", ''.join(stderr.readlines()))
    
    client.close()

# Input from user
hostname = input("Enter hostname: ")
username = input("Enter username: ")
command = input("Enter command to execute: ")

ssh_server(hostname, username, command)
