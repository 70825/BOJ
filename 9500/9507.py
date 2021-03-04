T=int(input())
def k(A):
    n=N[0]+N[1]+N[2]+N[3]
    N[3]=N[2]
    N[2]=N[1]
    N[1]=N[0]
    N[0]=n
    return N

for i in range(T):
    A=int(input())
    N = [4, 2, 1, 1]
    if A<=3:print(N[3-A])
    else:
        for j in range(A-3):k(A)
        print(N[0])