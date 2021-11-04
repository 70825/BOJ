n, q = map(int, input().split())

back = []
forward = []
page = -1

for i in range(q):
    arr = input().split()
    if arr[0] == 'B' and len(back):
        forward.append(page)
        page = back.pop()
    if arr[0] == 'F' and len(forward):
        back.append(page)
        page = forward.pop()
    if arr[0] == 'A':
        forward = []
        if page != -1: back.append(page)
        page = int(arr[1])
    if arr[0] == 'C':
        new_back = []
        count = [-1, 0]
        for j in range(len(back)):
            if count[0] != back[j]:
                new_back.append(back[j])
                count = [back[j], 1]
            else: continue
        back = new_back

print(page)
if len(back): print(*back[::-1])
else: print(-1)
if len(forward): print(*forward[::-1])
else: print(-1)