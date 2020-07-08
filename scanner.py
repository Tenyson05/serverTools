# Check for the bigger script from hackersploit on YT


import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("Using nmap version", scanner.nmap_version())
print("<---------------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP address you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
				1. SYNC ACK Scan
				2. UDP Scan
				3. COmprehensive Scan\n""")
print("You have selected option: ", resp)

if resp == '1':
	scanner.scan(ip_addr, '1-1024', '-v -sS')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Open Ports: ", scanner[ip_addr].all_tcp())
if resp == '2':
	scanner.scan(ip_addr, '1-1024', '-v -sU')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Open Ports: ", scanner[ip_addr].all_udp())
if resp == '3':
	scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Open Ports: ", scanner[ip_addr].all_tcp())
elif resp >= '4':
	print("Please enter a valid option")