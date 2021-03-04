N=int(input())
for i in range(N):
    N=int(input());A=str(input());B=str(input());s=0
    for j in range(N):
        if A[j]!=B[j]:s+=1
    print('Case '+str(i+1)+':',s)