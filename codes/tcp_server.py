#!/home/calypse/repos/python-networking/codes/bin/python3

import socket
import threading

# Setting up the IP and Port for the server to listen on
bind_ip = "0.0.0.0"
bind_port = 9999

# Create A Server Socket Object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

# Listen to maximum 5 connections
server.listen(5)

print("[*] Listening on: %s:%d" % (bind_ip, bind_port))

# Client Handling Thread
def handle_client(client_socket):
	# Print out what the client sends
	request = client_socket.recv(1024)
	print("[*] Received: %s" % request)

	# Send Back a Packet
	client_socket.send(b"ACK!")
	client_socket.close()

while True:
	client, addr = server.accept() # client = client socket object
									# addr[0] = client ip
									# addr[1] = client port
	print("[*] Accepted Connection From: %s:%d" % (addr[0], addr[1]))

	# Spin Up Our Client Thread to Handle Incoming Data
	client_handler = threading.Thread(target=handle_client, args=(client,))
									# target -> the function the thread will run
									# args -> arguments passed to the function
	client_handler.start()