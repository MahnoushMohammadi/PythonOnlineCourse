import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_256722.json'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))
info2 = js["comments"]
s = 0
for i in info2:
  n = i['count']
  s+=n
print s
