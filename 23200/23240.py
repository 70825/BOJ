m = int(input())
arr = [input().split() for i in range(m)]
color = []
val = []
move = [0] * m
ans = 0

for i in range(m):
    color.append(arr[i][0])
    val.append(int(arr[i][1]))

for i in range(m-1, -1, -1):
    if color[i] == 'G':
        move[i] += 1
        for j in range(i-1, -1, -1):
            move[j] += 2 ** (i - j - 1)
    elif color[i] == 'B': # 현재 move가 짝수인 경우 두 번 이동해야함. 홀수면 한 번 이동해야함
        if move[i] % 2 == 0 and val[i] != 1:
            if i == 0: ans -= 1
            move[i] += 2
            for j in range(i-1, -1, -1):
                move[j] += 2 ** (i - j)
        else:
            move[i] += 1
            for j in range(i-1, -1, -1):
                move[j] += 2 ** (i - j - 1)
    else: # 현재 move가 짝수인 경우 한 번 이동해야함. 홀수면 두 번 이동해야함
        if move[i] % 2 == 0 or val[i] == 1:
            move[i] += 1
            for j in range(i-1, -1, -1):
                move[j] += 2 ** (i - j - 1)
        else:
            if i == 0: ans -= 1
            move[i] += 2
            for j in range(i-1, -1, -1):
                move[j] += 2 ** (i - j)

for i in range(m):
    ans += val[i] * move[i]

print(ans)