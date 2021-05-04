import nmap
import sys

nm_scan = nmap.PortScanner()

print("\nRunning...\n")

nm_scanner = nm_scan.scan(sys.argv[1], "80", arguements="-O")

host_is_up = "THe Host is : " + nm_scanner['scan'][sys.argv[1]]['status']['state'] + ".\n"

port_open = "THe Port 80 is : " + nm_scanner['scan'][sys.argv[1]]['tcp']['status'] + ".\n"

method_scan = "The method of scanning is : "+ nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'] + ".\n"