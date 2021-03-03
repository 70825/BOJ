T=int(input())
D=[0];E='';F=''
k=1
for i in range(T):
    N=int(input())
    if D[0]<N:
        while D[0]!=N:
            D.insert(0,k);k+=1;F+='+\n'
    if D[0]==N:del D[0];F+='-\n'
if len(D)==1:
    print(F)
else:print('NO')