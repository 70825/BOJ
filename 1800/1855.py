K=int(input());S=input();D=[]
for i in range(len(S)//K):
    a=S[K*i:K*(i+1):]
    if i%2==0:D.append(a)
    else:D.append(a[::-1])
for i in range(K):
    for j in range(len(D)):print(D[j][i],end="")