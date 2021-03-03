R,B=map(int,input().split())
n=1
while n!=(R+B)//2:
    a=(R+B)//n
    if (a-2)*(n-2)==B:break
    n+=1
print(max(a,n),min(a,n))