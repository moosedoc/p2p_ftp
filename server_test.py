import socket
import os

DIR='./server_files/'

sock=socket.socket()

host=socket.gethostname()
port=5140

print 'Server start'
sock.bind((host, port))
sock.listen(5)
while True:
	conn, addr=sock.accept()
	print 'Connection from ... {0}'.format(addr)

	try:
		name=conn.recv(1024)
		with open(DIR+name, 'w') as f:
			l=conn.recv(1024)
			while l:
				print 'Message from {0}'.format(addr)
				f.write(l)
				l=conn.recv(1024)
			print 'File transfer success!'
	except: pass

sock.shutdown(socket.SHUT_WR)
