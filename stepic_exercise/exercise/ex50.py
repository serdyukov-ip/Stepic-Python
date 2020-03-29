import requests
with open('txt/files.txt', 'r') as file:
    s = file.readline().strip()
    r = requests.get(s)
while True:
    ss = "https://stepic.org/media/attachments/course67/3.6.3/" + r.text
    r = requests.get(ss)
    if len(r.text) > 20:
        break

with open('txt/files_result.txt', 'w') as out:
    out.write(str(r.text))

print('ok')