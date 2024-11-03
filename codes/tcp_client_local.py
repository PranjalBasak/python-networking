#!/home/calypse/repos/python-networking/codes/bin/python3
# Setting up the target server's details
import socket
target_host = "0.0.0.0"
target_port = 9999

# Create a Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = Standard IPv4 Address/hostname
# socket.SOCK_STREAM = TCP Client

# Connect the client to the server
client.connect((target_host, target_port))

# Send some data to the server
client.send(b"AAAAAAAAAAA")

# Receive Some Data
response = client.recv(4096)

print(response)

