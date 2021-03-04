a,b=map(int,input().split())
s=1
while a<=b:s*=a*(a+1)//2;a+=1
print(s%14579)