N,M=map(int,input().split())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
memo=[]
for i in range(N):
    if A[i]<B[i]:memo.append([A[i],B[i]])
memo.sort()
for i in range(len(memo)):
    if M<memo[i][0]:break
    M=M-memo[i][0]+memo[i][1]
print(M)