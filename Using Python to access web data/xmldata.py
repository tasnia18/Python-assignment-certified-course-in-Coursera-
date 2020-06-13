import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url ='http://py4e-data.dr-chuck.net/comments_438566.xml'
html = urllib.request.urlopen(url).read()
sum=0
nums=ET.fromstring(html)
lst=nums.findall('comments/comment')
for item in lst:
    num=int(item.find('count').text)
    sum=sum+num

print(sum)