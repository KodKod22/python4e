import urllib.request,urllib.parse
import json,ssl


url = input('Enter location: ')


print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data),'characters')
info = json.loads(data)
items = info['comments']
lst = list()
for item in items:
    lst.append(int(item['count']))

print(sum(lst))
# http://py4e-data.dr-chuck.net/comments_2096480.json