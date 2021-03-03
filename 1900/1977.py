M=int(input())
N=int(input())
ans=0
D=[]
for i in range(M,N+1):
    if i**0.5==int(i**0.5):
        ans+=i
        D.append(i)
if ans!=0:
    print(ans);print(min(D))
else:
    print(-1)