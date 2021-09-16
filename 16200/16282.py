arr = [n*(2**n-1) + (n-1) for n in range(2, 60)]
val = [i for i in range(1, 59)]

n = int(input())
for i in range(len(arr)):
    if n <= arr[i]:
        print(val[i])
        break