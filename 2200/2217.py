n=int(input())
D=sorted([int(input()) for i in range(n)])[::-1]
ans=0
for i in range(n):
    ans=max(ans,D[i]*(i+1))
print(ans)