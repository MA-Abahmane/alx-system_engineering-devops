Welcome to  my 0x08-networking_basics_2 directory
by: Mohamed Amine Abahmane

# Important commands to have in your ToolBox.

# ifconfig: 
Configures and displays network interfaces (Unix-based systems).
  Example: ifconfig eth0 up (brings up the Ethernet interface)

# telnet: 
Establishes a Telnet connection to a remote host using the Telnet protocol.
  Example: telnet example.com 80 (connects to port 80 of example.com)

# nc: 
Netcat (nc) is a versatile networking utility that can be used for various purposes such as port scanning, file transfers, and establishing TCP or UDP connections.
  Example: nc -v example.com 8080 (establishes a TCP connection to example.com on port 8080)

# cut: 
Selects specific fields from input by specifying a delimiter and field number.
  Example: netstat -an | cut -d":" -f2 (extracts the port numbers from netstat output)

# netstat: 
Displays active network connections, listening ports, and related network statistics.
  Example: netstat -a (displays all active connections and listening ports)

# ping: 
Sends ICMP echo requests to a specified IP address or domain name to check network connectivity and measure round-trip time.
  Example: ping google.com or ping 192.168.0.1

# awk: 
A versatile text processing tool that can be used for data extraction, manipulation, and reporting. It supports field and record-based operations.
  Example: netstat -an | awk '{print $1}' (prints the first column of netstat output)

# ip: 
A versatile command for configuring network interfaces, routing tables, and other IP-related settings (Unix-based systems).
  Example: ip address show (displays IP addresses of network interfaces)


These commands provide specific functionalities related to network configuration, troubleshooting, and data manipulation. Remember to consult the command's documentation for further details on their usage and available options.


