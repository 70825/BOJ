N=int(input())
X=int(input())
ans=0
for i in range(N):
    P1,P2=map(int,input().split())
    if abs(P2-P1)>X:
        P3=int(input())
        ans+=P3
    else:
        ans+=max(P1,P2)
print(ans)