D=[1,0,0]
N=str(input())
for i in range(len(N)):
    if N[i]=='A':t=D[0];D[0]=D[1];D[1]=t
    elif N[i]=='B':t=D[1];D[1]=D[2];D[2]=t
    else:t=D[2];D[2]=D[0];D[0]=t
for i in range(3):
    if D[i]==1:print(i+1)