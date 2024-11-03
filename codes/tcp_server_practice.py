#!/home/calypse/repos/python-networking/codes/bin/python3

import socket
import threading

# Set up the server IP and Port
bind_ip = "0.0.0.0"
bind_port = 9999

# Create A Server Socket Object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

# Listen to maximum 5 connections
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# Client Handling Thread
def handle_client(client_socket):
	request = client_socket.recv(1024)
	print("[*] Received %s" % request)

	# Send Back A Request
	client_socket.send(b"ACK!")
	client_socket.close()

while True:
	client_socket, addr = server.accept()
	print("[*] Accepted Connection From: %s:%d" % (addr[0], addr[1]))

	# Spin up the client thread to handle incoming data
	client_handler_thread = threading.Thread(target=handle_client, args = (client_socket,))
	client_handler_thread.start()