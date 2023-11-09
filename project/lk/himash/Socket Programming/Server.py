# Socket programming :
# Socket programming is a way of connecting two nodes on a network to communicate with each other.
# One socket(node) listens on a particular port at an IP, while the other socket reaches out to the
# other to form a connection. The server forms the listener socket while the client reaches out to the server.
# They are the real backbones behind web browsing. In simpler terms, there is a server and a client.

# An example script to connect to using socket
# programming in Python

# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print ("Socket successfully created")
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 9999
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('localhost', port))
print ("socket binded to %s" %(port))
# put the socket into listening mode
s.listen(5)
print ("socket is listening")
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    clientReq = c.recv(1024).decode()
    print('Got connection from', addr, clientReq)
    response = 'Thank you for connecting... ' + clientReq
    # send a thank you message to the client. encoding to send byte type. below both patters are valid.
    # c.send(response.encode())
    c.send(bytes(response, 'UTF-8'))
    # Close the connection with the client
    c.close()
    # Breaking once connection closed
    break



