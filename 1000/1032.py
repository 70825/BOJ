T=int(input());D=[]
for i in range(T):
    D.append(str(input()))
for i in range(len(D[0])):
    E=[]
    for j in range(T):
        E.append(D[j-1][i])
    F=list(set(E))
    if len(F)==1:print(D[0][i],end="")
    else:print('?',end="")