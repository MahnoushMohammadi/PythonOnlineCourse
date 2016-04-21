import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_256718.xml'
address = raw_input('Enter location: ')
url = serviceurl 
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
s = 0
t = 0
for i in counts:
    num = i.find('count').text
    num2 = int(num)
    s += num2
    t += 1
print 'Count:' , t
print 'Sum:' , s