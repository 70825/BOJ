N,M=map(int,input().split())
arr=[*map(int,input().split())]
memo=[]
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k]<=M:
                memo.append(arr[i]+arr[j]+arr[k])
print(max(memo))