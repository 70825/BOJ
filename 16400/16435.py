N,L=map(int,input().split())
A=input().split()
D=[]
for i in range(N):D.append(int(A[i]))
D.sort()
for i in range(N):
    if D[i]<=L:L+=1
    else:break
print(L)