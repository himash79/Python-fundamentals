import socket

try:
    c = socket.socket()

    c.connect(('localhost', 9999))
    name = input('Enter username : ')
    c.send(bytes(name, 'UTF-8'))
    print(c.recv(1024).decode())
except Exception as e:
    print('Exception occur', e)