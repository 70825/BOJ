memo=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(int(input())):
    x=[*map(int,input().split())]
    for j in range(3):
        if x[j]==3:memo[j][0]+=3;memo[j][1]+=1
        elif x[j]==2:memo[j][0]+=2;memo[j][2]+=1
        else:memo[j][0]+=1;memo[j][3]+=1
k=sorted(memo,reverse=True)[0]
a=0;b=0
for i in range(3):
    if memo[i]==k:
        a=i;b+=1
if b==1:print(a+1,memo[a][0])
else:print(0,memo[a][0])