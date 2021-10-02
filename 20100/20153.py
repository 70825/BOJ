input =__import__('sys').stdin.readline
n = int(input())
arr = [*map(int, input().split())]
expo = [0] * 23
for i in range(n):
    val = bin(arr[i])[2:]
    for j in range(1, len(val)+1):
        if val[-j] == '1': expo[j-1] += 1
ans = 0
for i in range(23):
    if expo[i] % 2 : ans += 2 ** i
for i in range(n):
    val = bin(arr[i])[2:]
    for j in range(1, len(val) + 1):
        if val[-j] == '1': expo[j-1] -= 1
    new_ans = 0
    for j in range(23):
        if expo[j] % 2: new_ans += 2 ** j
    ans = max(ans, new_ans)
    for j in range(1, len(val) + 1):
        if val[-j] == '1': expo[j-1] += 1
print(str(ans)+str(ans))