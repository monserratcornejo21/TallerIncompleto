import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
message = b'This is the message.  It will be repeated.'
print('sending {!r}'.format(message))
sock.send(message)
datos=sock.recv(100)
print(datos)