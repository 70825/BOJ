arr = [1] * 51
MOD = 10**9 + 7
for i in range(2, 51):
    arr[i] = (arr[i] + arr[i-1] + arr[i-2]) % MOD
n = int(input())
print(arr[n])