n=int(input())
k=int(input())
d=0;s=n
while d!=k:
    s+=n*10**(d+1)
    d+=1
print(s)