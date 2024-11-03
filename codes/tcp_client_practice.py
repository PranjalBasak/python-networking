#!/home/calypse/repos/python-networking/codes/bin/python3

import socket

# Let's make a naive client
target_host = "0.0.0.0"
target_port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((target_host, target_port))

# Send data to the server
client.send(b"SYN")

# Get Response
response = client.recv(4096)
print(response)