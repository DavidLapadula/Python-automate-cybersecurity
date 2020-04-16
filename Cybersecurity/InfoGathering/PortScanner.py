import nmap, sys

target = str(sys.argv[1])
ports = [21, 22, 80, 139, 443, 8080]

scan_v = nmap.PortScanner()

for port in ports:
    portscan = scan_v.scan(target, str(port))
    print("Port Data " + portscan)