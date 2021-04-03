t = int(input())
arr = list(map(int,input().split()))
for i in range(len(arr)):
    a = arr[i]//3
    b = arr[i]//7
    c = arr[i]//21
    ans = (a*(a+1)//2)*3 + (b*(b+1)//2)*7 - (c*(c+1)//2)*21
    print(ans)