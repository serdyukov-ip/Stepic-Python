from urllib.request import urlopen
import re
import collections
html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
s = str(html)

regex = '<code>(.*?)</code>'
l = sorted(re.findall(regex, s))

for i in collections.Counter(l).most_common():
    if i[1] > 3:
        print(i[0], ' ', end='')
