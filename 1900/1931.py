n=int(input())
D=sorted([[*map(int,input().split())] for _ in range(n)],key= lambda a:[a[1],[a[0]]])
t=0;ans=0
for i in range(n):
    if D[i][0]>=t:t=D[i][1];ans+=1
print(ans)