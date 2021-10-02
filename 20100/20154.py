from collections import deque
input = __import__('sys').stdin.readline
alphabet = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

arr = [*input().strip()]
q = deque()
for i in range(len(arr)):
    q.append(alphabet[ord(arr[i]) - ord('A')])
nq = deque()
while q:
    if len(q) == 1:nq.append(q.pop())
    else:
        x, y = q.popleft(), q.popleft()
        nq.append((x + y) % 10)
    if not q:
        if len(nq) == 1:break
        else: q = nq; nq=deque()
if nq[0] % 2: print("I'm a winner!")
else: print("You're the winner?")