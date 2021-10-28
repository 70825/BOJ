n, m = map(int, input().split())
card = [*map(int, input().split())] # 0 : 앞면, 1 : 뒷면
val = 0
for i in range(m):
    k = int(input())
    if card[val] <= k: val = (val + 1) % 2
print(card[val])