n = int(input())
arr = sorted([[*map(int, input().split())] + [_+1] for _ in range(n)], key=lambda x:(x[0]**2+x[1]**2), reverse=True)
for i in range(n): print(arr[i][2])