for i in range(int(input())):
    A,B=map(int,input().split())
    A_memo=[];B_memo=[]
    ans=0
    while A!=0:
        A_memo.append(A);A//=2
    while B!=0:
        B_memo.append(B);B//=2
    N=min(len(A_memo),len(B_memo))
    A_memo=A_memo[::-1];B_memo=B_memo[::-1]
    for j in range(N):
        if A_memo[j]!=B_memo[j]:ans=A_memo[j-1];break
    if ans==0:ans=A_memo[N-1]
    print(ans*10)