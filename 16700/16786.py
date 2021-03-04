N=int(input())
memo_N=[*map(int,input().split())]
M=int(input())
memo_M=[*map(int,input().split())]
for i in range(M):
    S=memo_N[memo_M[i]-1]
    if S+1 not in memo_N and S<2019:memo_N[memo_M[i]-1]+=1
for i in memo_N:print(i)