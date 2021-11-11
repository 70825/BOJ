n, l, h = map(int, input().split())
arr = sorted([*map(int, input().split())])
arr = arr[l:len(arr)-h]
print(sum(arr)/len(arr))