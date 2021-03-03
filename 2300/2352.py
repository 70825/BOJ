from bisect import bisect_left
n=int(input())
D=[*map(int,input().split())]
arr=[D[0]]
for i in range(1,n):
    if arr[-1]>=D[i]:
        k=bisect_left(arr,D[i])
        arr[k]=D[i]
    else:arr.append(D[i])
print(len(arr))