from bisect import bisect_left
arr=[0]
n=int(input())
D=[*map(int,input().split())]
for i in range(n):
    if arr[-1]>D[i]:
        arr[bisect_left(arr,D[i])]=D[i]
    else:arr.append(D[i])
print(n-(len(arr)-1))