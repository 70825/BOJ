def go(idx, prev, c):
    global res
    if idx == 10:
        score = sum(1 for i in range(10) if answer[i] == arr[i])
        if score >= 5: res += 1
        return

    for i in range(5):
        if prev != i+1:
            answer[idx] = i+1
            go(idx+1, i+1, 1)
        if prev == i+1 and c == 1:
            answer[idx] = i+1
            go(idx+1, i+1, 2)


arr = [*map(int, input().split())]
res = 0
answer = [0] * 10
go(0, 0, 0)
print(res)