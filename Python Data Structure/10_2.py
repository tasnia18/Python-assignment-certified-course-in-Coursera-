"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the 
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

l = open("mbox-short.txt")
count=dict()
for line in l:
    line = line.rstrip()
    if len(line) <1:
        continue
    words = line.split()
    if words[0] != "From": continue
    else:
        d=words[5]
        h=d.split(':')
        hr=h[0]
        count[hr]=count.get(hr,0)+1
lst=list()
for k,v in count.items():
    lst.append((k,v))

lst=sorted(lst)

for k,v in lst:
    print(k,v)