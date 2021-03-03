k=1
while 1:
    memo = []
    N = int(input())
    if N==0:break
    for i in range(N):
        memo.append(input())
    print('SET',k)
    for i in range(0, N, 2):
        print(memo[i])
    for i in reversed(range(1, N, 2)):
        print(memo[i])
    k+=1