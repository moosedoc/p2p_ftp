import socket

sock=socket.socket()

host=socket.gethostname()
port=5136

print 'Client starting'

sock.connect((host, port))
sock.send('I am the client')

while True:
	msg=raw_input()
	if msg == 'q':
		break
	sock.send(msg)

sock.send('Client disconnecting')

# sock.shutdown(socket.SHUT_WR)
