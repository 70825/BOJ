N=int(input())
D=[];card=[]
for i in range(N):D.append(i+1)
for i in range(N):
    card.append(D[0]);D.pop(0)
    if len(D)!=0:D.append(D[0]);D.pop(0)
print(' '.join(map(str,card)))