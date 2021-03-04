for i in range(int(input())):
    memo=[]
    for j in range(26):
        memo.append(chr(j+97))
    N=int(input())
    D=[*map(int,input().split())]
    k=''
    for j in range(N):
        k+=memo[D[j]]
        ans=memo[D[j]]
        memo.remove(ans)
        memo.insert(0,ans)
    print(k)