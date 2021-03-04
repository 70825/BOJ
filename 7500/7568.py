memo=[]
D=[]
N=int(input())
for i in range(N):
    n,m=map(int,input().split())
    memo.append([n,m])
for i in range(N):
    t=1
    for j in range(N):
        if j!=i and memo[i][0]<memo[j][0] and memo[i][1]<memo[j][1]:
            t+=1
    D.append(t)
print(' '.join(map(str,D)))