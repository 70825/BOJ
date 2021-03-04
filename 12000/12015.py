from bisect import bisect_left
n=int(input())
D=[*map(int,input().split())]
arr=[0]
for i in range(n):
    if arr[-1]>=D[i]:
        k=bisect_left(arr,D[i])
        arr[k]=D[i]
    else:arr.append(D[i])
print(len(arr)-1)