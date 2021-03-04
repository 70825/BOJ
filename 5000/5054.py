T=int(input())
for i in range(T):
    N=int(input())
    B=input().split()
    for j in range(N):
        B[j]=int(B[j])
    print((max(B)-min(B))*2)