for _ in range(int(input())):
    n=int(input())
    D=[*map(int,input().split())]
    k=int(input())
    S=[0]*(k+1);S[0]=1
    for i in D:
        for j in range(k+1):
            if j-i>=0:S[j]+=S[j-i]
    print(S[k])