import requests

with open('txt/requests.txt', 'r') as file:
    s = file.readline().strip()
r = requests.get(s)
r = r.text
r = r.splitlines()
with open('txt/requests_result.txt', 'w') as out:
    out.write(str(len(r)))
