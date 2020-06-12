import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url ='http://py4e-data.dr-chuck.net/known_by_Sherwyn.html'
t=7 #times
while t>0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    names=[]
    link=[]
    for tag in tags:
        link.append(tag.get('href', None))
        names.append(tag.text)
    #for name in names:
    print(names[17]) #position-1 for list starts from 0
    url=link[17]
    t=t-1