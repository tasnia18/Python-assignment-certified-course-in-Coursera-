import urllib.request, urllib.parse, urllib.error
import json
url ='http://py4e-data.dr-chuck.net/comments_438567.json'
html = urllib.request.urlopen(url).read()
info = json.loads(html)
#print(info['comments'][0]['count'])
#print(json.dumps(info, indent=4))
i=0
sum=0
while True:
    try:
        p = info['comments'][i]['count']
        n = info['comments'][i]['name']
        i=i+1
        sum=sum+p
    except:
        break
print(sum)