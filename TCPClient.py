import socket

#cretae socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 
host = socket.gethostname()

port = 444

# Subsititue the host with the server IP
clientSocket.connect(('192.169.1.107', port))

#Receiving a maximum of 1024 bytes
message = clientSocket.recv(1024)

clientSocket.close()

print(message.decode('ascii'))