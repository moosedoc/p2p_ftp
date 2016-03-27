import socket

sock=socket.socket()

host=socket.gethostname()
port=5136

print 'Server start'

sock.bind((host, port))
sock.listen(5)
while True:
	conn, addr=sock.accept()
	print 'Connection from ... {0}'.format(addr)

	try:
		l=conn.recv(1024)
		while l:
			print l
			l=conn.recv(1024)
	except: pass

conn.send('Take care {0}'.format(addr))
conn.close()
