""" 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of 
mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent 
the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of 
times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a 
maximum loop to find the most prolific committer."""

l = open("mbox-short.txt")
count=dict()
for line in l:
    line = line.rstrip()
    if line == "": continue

    words = line.split()
    if words[0] != "From": continue
    else:
        email=words[1]
        count[email]=count.get(email,0)+1

V= None
K = None
for k,v in count.items():
    if V is None or v>V:
        K=k
        V=v
print(K,V)
