from bisect import bisect_left
input=__import__('sys').stdin.readline
n=int(input())
D=[*map(int,input().split())]
arr=[D[0]]
res=[[arr[0],0]]
for i in range(1,n):
    if arr[-1]>=D[i]:
        k=bisect_left(arr,D[i])
        arr[k]=D[i]
        res.append([D[i],k])
    else:
        arr.append(D[i])
        res.append([D[i],len(arr)-1])
ans=[]
k=len(arr)-1
for i in range(n-1,-1,-1):
    if res[i][1]==k:ans.append(res[i][0]);k-=1
print(len(arr))
print(*ans[::-1])