n = int(input())
arr = sorted([[*input().split()] for _ in range(n)], key=lambda x:int(x[1]))
print(arr[0][0])