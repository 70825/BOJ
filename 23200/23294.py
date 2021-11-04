input = __import__('sys').stdin.readline
from collections import deque
n, q, c = map(int, input().split())
cache = [*map(int, input().split())]

back = deque()
back_value = deque()
forward = deque()
forward_value = deque()
page = -1

for i in range(q):
    arr = input().strip().split()
    if arr[0] == 'B' and len(back):
        forward.append(page)
        forward_value.append(cache[page-1])
        page = back.pop()
        back_value.pop()
    if arr[0] == 'F' and len(forward):
        back.append(page)
        back_value.append(cache[page-1])
        page = forward.pop()
        forward_value.pop()
    if arr[0] == 'A':
        forward = deque()
        if page != -1:
            back.append(page)
            back_value.append(cache[page-1])
        page = int(arr[1])
        if sum(back_value) + cache[page-1] > c:
            while sum(back_value) + cache[page-1] > c:
                back.popleft()
                back_value.popleft()
        page = int(arr[1])
    if arr[0] == 'C':
        new_back = deque()
        new_back_value = deque()
        count = [-1, 0]
        for j in range(len(back)):
            if count[0] != back[j]:
                new_back.append(back[j])
                new_back_value.append(back_value[j])
                count = [back[j], 1]
            else: continue
        back = new_back
        back_value = new_back_value

print(page)
if len(back): print(*list(back)[::-1])
else: print(-1)
if len(forward): print(*list(forward)[::-1])
else: print(-1)