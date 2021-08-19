n = int(input())
s = input()
arr = [*map(int, input().split())]
stone = []
score = []
color = 0
same = []
for i in range(n):
    if s[color] == s[i]: same.append(arr[i])
    else:
        big = color
        for j in range(color, i):
            if arr[j] > arr[big]: big = j
        stone.append([s[big], arr[big]])
        same = [arr[i]]
        color = i
if len(stone) <= 1:
    print(0)
    exit()
stone.pop(0)
stone.sort(key=lambda x:-x[1])
k = len(stone) // 2
print(sum(stone[i][1] for i in range(k + 1 if len(stone) % 2 else k)))