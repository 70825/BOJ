N,S=map(int,input().split())
D=[];k=0
for i in range(N):
    D.append(int(input()))
for i in range(N-1):
    for j in range(i+1,N):
        if D[i]+D[j]<=S:k+=1
print(k)