A,B,C=map(int,input().split())
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
memo=[0]*max(a,b,c,d,e,f)
k=min(a,b,c,d,e,f)-1
ans=0
for i in range(a-k,b-k):memo[i]+=1
for i in range(c-k,d-k):memo[i]+=1
for i in range(e-k,f-k):memo[i]+=1
ans+=memo.count(1)*A
ans+=memo.count(2)*B*2
ans+=memo.count(3)*C*3
print(ans)