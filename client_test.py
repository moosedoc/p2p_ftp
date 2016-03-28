import socket
import os

sock=socket.socket()

host=socket.gethostname()
port=5140

print 'Client starting'

sock.connect((host, port))
# sock.send('I am the client')

while True:
	file=raw_input()
	if os.path.exists(file):
		with open(file, 'r') as f:
			l=f.read(1024)
			while l:
				print 'Sending...'
				sock.send(l)
				l=f.read(1024)
			print 'File sent!'
		break
	else:
		print 'error: {0} does not exist'.format(file)

sock.send('Client disconnecting')
sock.shutdown(socket.SHUT_WR)
