E,S,M=map(int,input().split())
a=b=c=1
year=1
while a!=E or b!=S or c!=M:
    a+=1;b+=1;c+=1
    if a==16:a-=15
    if b==29:b-=28
    if c==20:c-=19
    year+=1
print(year)