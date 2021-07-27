arr = [*input()]
ans = ['.'] * len(arr)

val = 0
for i in range(len(arr)):
    if arr[i] == 'X': val += 1
    if arr[i] == '.' and val % 2: print(-1); exit()
    if arr[i] == '.' and val == 2: ans[i-2:i] = ['B']*2; val = 0
    if val == 4: ans[i-3:i+1] = ['A']*4; val = 0
if val == 2: ans[-2:] = ['B']*2
print([''.join(ans), -1][val % 2])