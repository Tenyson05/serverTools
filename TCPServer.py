# Encode the message

import socket

#Creating the socket object 
# AF_NET porotocol use for communcation IPV4 or IPV6
# Socket type - sock_stream or sock_dgram
# These depened on type of protocol. sock_stream means you are using connection oriented protocol such as TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host is the server IP
host = socket.gethostname()
print(host)

# Port to listen on
port = 44

#Binding to socket
serverSocket.bind((host, port))

#Starting TCP listener
serverSocket.listen(4)

while True:
	# Starting the connection
	clientSocket, address = serverSocket.accept()

	print("Received connection from %s",  str(address))

	# Message sent to client after successful connection
	message = "Hello! Thank you for connection to the server" + "\r\n"
	clientSocket.send(message.encode('ascii'))

	clientSocket.close()

