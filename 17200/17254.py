n, m = map(int, input().split())
arr = sorted([input().split() for _ in range(m)], key=lambda x: [int(x[1]), int(x[0])])
print(''.join([arr[i][2] for i in range(m)]))