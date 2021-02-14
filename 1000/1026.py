N=int(input());A=list(map(int,input().split()));B=list(map(int,input().split()));A.sort();B.sort(reverse=True);k=0
for i in range(N):k+=A[i]*B[i]
print(k)