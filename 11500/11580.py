N=int(input())
S=input()
count=1
memo=[[0,0]]
now=[0,0]
for i in range(N):
    if S[i]=='N':now[1]+=1
    elif S[i]=='S':now[1]-=1
    elif S[i]=='E':now[0]+=1
    else:now[0]-=1
    if memo.count([now[0],now[1]])==0:
        memo.append([now[0],now[1]])
        count+=1
print(count)