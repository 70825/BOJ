N,M=map(int,input().split())
Paper=[]
for i in range(N):
    Paper.append([*map(int,input().split())])
k=0
for i in range(N):
    for j in range(M-3):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i][j+2]+Paper[i][j+3]
        if ans>k:k=ans
for i in range(N-3):
    for j in range(M):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i+2][j]+Paper[i+3][j]
        if ans > k: k = ans
for i in range(N-1):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i+1][j]+Paper[i+1][j+1]
        if ans > k: k = ans
for i in range(N-2):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i+2][j]+Paper[i+2][j+1]
        if ans > k: k = ans
for i in range(N-1):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i][j+1]+Paper[i][j+2]
        if ans > k: k = ans
for i in range(N-2):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i+1][j+1]+Paper[i+2][j+1]
        if ans > k: k = ans
for i in range(1,N):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i][j+2]+Paper[i-1][j+2]
        if ans > k: k = ans
for i in range(2,N):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i-1][j+1]+Paper[i-2][j+1]
        if ans > k: k = ans
for i in range(N-1):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i+1][j+1]+Paper[i+1][j+2]
        if ans > k: k = ans
for i in range(N-2):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i+2][j]+Paper[i][j+1]
        if ans > k: k = ans
for i in range(N-1):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i][j+2]+Paper[i+1][j+2]
        if ans > k: k = ans
for i in range(N-2):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i+1][j+1]+Paper[i+2][j+1]
        if ans > k: k = ans
for i in range(1,N):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i-1][j+1]+Paper[i-1][j+2]
        if ans > k: k = ans
for i in range(2,N):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i-1][j]+Paper[i-1][j+1]+Paper[i-2][j+1]
        if ans > k: k = ans
for i in range(2,N):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i-1][j]+Paper[i-1][j+1]+Paper[i-2][j+1]
        if ans > k: k = ans
for i in range(N-1):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i+1][j+1]+Paper[i+1][j+2]
        if ans > k: k = ans
for i in range(1,N):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i][j+2]+Paper[i-1][j+1]
        if ans > k: k = ans
for i in range(1,N-1):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i-1][j+1]+Paper[i+1][j+1]
        if ans > k: k = ans
for i in range(N-2):
    for j in range(M-1):
        ans=Paper[i][j]+Paper[i+1][j]+Paper[i+2][j]+Paper[i+1][j+1]
        if ans > k: k = ans
for i in range(N-1):
    for j in range(M-2):
        ans=Paper[i][j]+Paper[i][j+1]+Paper[i][j+2]+Paper[i+1][j+1]
        if ans > k: k = ans
print(k)