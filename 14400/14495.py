D=[2,1,1,1]
def f(A):k=D[0]+D[2];D[3]=D[2];D[2]=D[1];D[1]=D[0];D[0]=k;return D
N=int(input())
if N<=4:print(D[4-N])
else:
    for i in range(N-4):f(D)
    print(D[0])