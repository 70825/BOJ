D=[1]*(int(input())-1)
T=int(input());k=1
for i in range(T):
    A,B=map(int,input().split())
    for j in range(A-1,B-1):D[j]=0
for i in range(len(D)):
    if D[i]==1:k+=1
print(k)