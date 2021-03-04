for _ in range(int(input())):
    n,m=map(int,input().split())
    D,ans={},0
    for i in range(n):
        D[input()]=0
    for i in range(m):
        A=input().split()
        D[A[0]]+=int(A[1])
    for i in D.keys():
        if D[i]==max(D.values()):ans+=1;k=i
    if ans==1:print('VOTE {}: THE WINNER IS {} {}'.format(_+1,k,D[k]))
    else:print('VOTE {}: THERE IS A DILEMMA'.format(_+1))