import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby = socket.gethostbyname(sys.argv[1])
print("\n THE ip ADDRESS OF " + sys.argv[1]+" is: "+ gethostby +"\n")

#ipinfo.io --- API I'll use

req_two = requests.get("https://ipinfo.io/"+gethostby+"/json")
resp = json.loads(req_two.text)

print("Location: "+ resp["loc"])
print("Region: "+ resp["region"])
print("City: "+ resp["city"])
print("Country: "+ resp["country"])
