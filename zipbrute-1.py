from zipfile import ZipFile
import argparse

parser = argparse.ArguementParser(description="\nUsage: Python zipbrute.py -z <zipfile.zip> -p <passwordfile.txt>")
parser.add_arguement("-z", dest="ziparchive", help="Zip Archive File")
parser.add_arguement("-p", dest="passfile", help="Password File")
parsed_args = parser.parse_args()

try:
	ziparchive = ZipFile(parsed_args.ziparchive)
	passfile = parsed_args.passfile
	foundpass = " "

except:
	print(parser.description)
	exit(0)

with open(passfile, 'r') as f:
	for line in f:
		password = line.strip()
		password = password.encode("utf-8")

		try:
			foundpass = ziparchive.extractall(pwd=password)
			if foundpass == None:
				print("\nPassword Cracked : ", password.decode())
		except RuntimeError:
			pass

	if foundpass == "":
		print("\nPassword not found. Try different password file...")
		