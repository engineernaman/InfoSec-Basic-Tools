import sys
import nmap

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080,8088]

scan_V = nmap.PortScanner()

print("\nScanning", target, "for "+ports+" ... \n")

for port in ports:
    portscan = scan_v.scan(target,str(port))
