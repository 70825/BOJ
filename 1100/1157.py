a={};b="ABCDEFGHIJKLMNOPQRSTUVWXYZ";c=input().upper()
for x in b:
    a[x]=c.count(x)
max_=max(a.values());c=0;d='';
for y in a.keys():
    if max_ == a[y]:c+=1;d=y
if c == 1:print(d)
else:print("?")