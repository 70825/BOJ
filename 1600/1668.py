D=[]
n=int(input())
for i in range(n):
    D.append(int(input()))
left,right=0,0
ans=0
for i in range(n):
    if D[i]>left:ans+=1;left=D[i]
print(ans);ans=0
for i in range(n-1,-1,-1):
    if D[i]>right:ans+=1;right=D[i]
print(ans)