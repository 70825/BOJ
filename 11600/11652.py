D={}
for i in range(int(input())):
    k=int(input())
    if k not in D:D[k]=1
    else:D[k]+=1
d=max(sorted(D.values()))
D=sorted(D.items())
for i in range(len(D)):
    if D[i][1]==d:
        print(D[i][0]);break