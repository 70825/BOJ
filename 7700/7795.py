for _ in range(int(input())):
    ans=0;input()
    A=sorted([*map(int,input().split())])
    B=sorted([*map(int,input().split())])
    a,b=0,0
    while a!=len(A) and b!=len(B):
        if A[a]>B[b]:ans+=len(A)-a;b+=1
        else:a+=1
    print(ans)