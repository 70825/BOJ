for i in range(int(input())):
    D={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    S=str(input());k=0
    for j in range(len(S)):D[S[j]]+=1
    for j in range(10):
        if D[str(j)]!=0:k+=1
    print(k)