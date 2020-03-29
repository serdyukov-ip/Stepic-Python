import xmltodict

fin = open('xml/map3.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
count = 1
dct = xmltodict.parse(xml)
tags = [item for item in dct['osm']]
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    count += 1

print(count)
