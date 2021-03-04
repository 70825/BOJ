for _ in range(int(input())):
    input();ans=0
    A=sorted([*map(int,input().split())])
    B=sorted([*map(int,input().split())],reverse=True)
    for i in range(len(A)):ans+=A[i]*B[i]
    print('Case #{}: {}'.format(_+1,ans))