import xmltodict

fin = open('xml/map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

contains = 0
not_contained = 0

dct = xmltodict.parse(xml)
for node in dct['osm']['node']:
    if 'tag' in node:
        contains+= 1
    else:
        not_contained+= 1

print(contains, not_contained)
