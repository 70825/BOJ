input = __import__('sys').stdin.readline
N = 400001

w, n = map(int, input().split())
arr = [*map(int, input().split())]
sum_arr1 = [-1] * N
sum_arr2 = [-1] * N

for i in range(n):
    for j in range(i+1, n):
        val = arr[i] + arr[j]
        if sum_arr1[val] == -1:
            sum_arr1[val] = i
            sum_arr2[val] = j
for i in range(n):
    for j in range(i+1, n):
        val = w - arr[i] - arr[j]
        if val >= N or val < 0 or sum_arr1[val] == -1: continue
        if sum_arr1[val] != i and sum_arr1[val] != j and sum_arr2[val] != i and sum_arr2[val] != j:
            print('YES')
            exit()
print('NO')