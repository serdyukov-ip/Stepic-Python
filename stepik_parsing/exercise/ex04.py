from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html').read().decode('utf-8')
s = str(html)
su = 0
soup = BeautifulSoup(s, 'html.parser')
for td in soup.select('td'):
    su += int(td.text)
print(su)