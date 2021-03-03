for _ in range(int(input())):
    N,M=map(int,input().split())
    memo=[*map(int,input().split())]
    Queue=[]
    k=0;i=0
    for j in range(N):
        Queue.append([memo[j],j])
    while 1:
        if Queue[i][0]==max(memo):
            k+=1
            if Queue[i][1]==M:break
            Queue.pop(i)
            memo.remove(max(memo))
        else:i+=1
        if i==len(Queue):i=0
    print(k)