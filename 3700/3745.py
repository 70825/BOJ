from bisect import bisect_left
while 1:
    try:
        n=int(input())
        D=[*map(int,input().split())]
        arr=[0]
        for i in range(n):
            if arr[-1]>=D[i]:arr[bisect_left(arr,D[i])]=D[i]
            else:arr.append(D[i])
        print(len(arr)-1)
    except EOFError:break