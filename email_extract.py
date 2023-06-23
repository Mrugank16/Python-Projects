import re

file=open("email_text.txt","r")

for line in file:
    s=line.strip()
    reg=re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",s)
    print(reg)