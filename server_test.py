import socket
import os

PATH='./server_files/file_{0}.txt'

sock=socket.socket()

host=socket.gethostname()
port=5140

file_num=0

print 'Server start'
sock.bind((host, port))
sock.listen(5)
while True:
	conn, addr=sock.accept()
	print 'Connection from ... {0}'.format(addr)

	while os.path.exists(PATH.format(file_num)):
		file_num+=1

	try:
		l=conn.recv(1024)
		with open(PATH.format(file_num), 'w') as f:
			while l:
				print 'Message from {0}'.format(addr)
				f.write(l)
				l=conn.recv(1024)
			print 'File transfer success!'
	except: pass

sock.shutdown(socket.SHUT_WR)


