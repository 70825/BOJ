n = int(input())
arr = []
for i in range(n):
    a,b = input().split()
    arr.append([a,int(b)])
arr.sort(key=lambda a:[-a[1],a[0]])
print(arr[0][0])