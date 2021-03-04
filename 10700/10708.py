N=int(input())
M=int(input())
D=[*map(int,input().split())]
memo=[]
for i in range(M):
    memo.append([*map(int,input().split())])
score=[0]*N
for i in range(M):
    t_score=0
    for j in range(N):
        if (j+1)!=D[i] and memo[i][j]==D[i]:score[j]+=1
        else:t_score+=1
    score[D[i]-1]+=t_score
for i in score:print(i)