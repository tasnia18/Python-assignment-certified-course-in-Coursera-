import re
file= open('actual')
sum=0
c=0
for line in file:
    line=line.rstrip()
    if len(line)<1:
        continue
    else:
            num = re.findall('([0-9]+)', line)

            if len(num)<1:
                continue
            else:
                for n in num:
                    s = int(n)
                    c = c + 1
                    sum=sum+s

print(c)
print(sum)