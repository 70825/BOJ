M,N=map(int,input().split())
memo=[0]*10
for i in range(M,N+1,1):
    for j in range(len(str(i))):memo[int(str(i)[j])]+=1
print(' '.join(map(str,memo)))