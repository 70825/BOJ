n,m=map(int,input().split())
D=[[0]*4 for _ in range(m)] # ACGT
for i in range(n):
    k=input()
    for j in range(m):
        if k[j]=='A':D[j][0]+=1
        elif k[j]=='C':D[j][1]+=1
        elif k[j]=='G':D[j][2]+=1
        else:D[j][3]+=1
ans='';t=0
for i in range(m):
    if D[i][0]==max(D[i]):ans+='A'
    elif D[i][1]==max(D[i]):ans+='C'
    elif D[i][2]==max(D[i]):ans+='G'
    else:ans+='T'
    t+=sum(D[i])-max(D[i])
print(ans)
print(t)