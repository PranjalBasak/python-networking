#!/home/calypse/repos/python-networking/codes/bin/python3
import socket 

host = "0.0.0.0"
port = 9999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host, port))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print(f"Connected by {addr}")
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)
