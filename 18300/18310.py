n = int(input())
arr = sorted([*map(int,input().split())])
if n % 2: print(arr[n//2])
else:print(arr[(n-1)//2])