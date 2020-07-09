import socket

def banner(ip, port):
	s = socket.socket()
	s.connect((ip, int(port)))
	# s.settimeout(5)
	print(s.recv(1024))

def main():
	ip = input("Please enter an IP: ")
	port = str(input("Please enter the port number: "))
	banner(ip, port)

main()