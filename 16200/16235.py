from collections import deque
input = __import__('sys').stdin.readline

n,m,k = map(int,input().split())
A = [[*map(int,input().split())] for _ in range(n)]
MAP = [[5]*n for _ in range(n)]
Tree = [[[] for __ in range(n)] for _ in range(n)]
Dead_Tree = [[0]*n for _ in range(n)]
Alive_Tree = [[deque() for __ in range(n)] for _ in range(n)]
Five_Tree = [[0]*n for _ in range(n)]

for i in range(m):
    x,y,z = map(int,input().split())
    x-=1; y-=1
    Tree[x][y].append(z)
for i in range(n):
    for j in range(n):
        Tree[i][j].sort()
        Tree[i][j] = deque(Tree[i][j])

def init():
    for i in range(n):
        for j in range(n):
            Alive_Tree[i][j] = deque()
            Dead_Tree[i][j] = 0
            Five_Tree[i][j] = 0

#봄,여름
def spring_summer():
    for i in range(n):
        for j in range(n):
            for k in range(len(Tree[i][j])):
                x = Tree[i][j].popleft()
                if MAP[i][j] < x:
                    Dead_Tree[i][j] += x//2
                else:
                    MAP[i][j] -= x
                    if (x+1) % 5 == 0: Five_Tree[i][j] += 1
                    Alive_Tree[i][j].append(x+1)
            Tree[i][j] = deque(Alive_Tree[i][j])
            MAP[i][j] += Dead_Tree[i][j]

#가을,겨울
def fall_winter():
    dx,dy = [1,1,1,-1,-1,-1,0,0],[-1,0,1,-1,0,1,-1,1]
    for i in range(n):
        for j in range(n):
            if Five_Tree[i][j] != 0:
                for k in range(8):
                    x, y = i+dx[k], j+dy[k]
                    if 0<=x<n and 0<=y<n:
                        for z in range(Five_Tree[i][j]): Tree[x][y].appendleft(1)
            MAP[i][j] += A[i][j]

while k:
    k -= 1
    spring_summer()
    fall_winter()
    init()
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(Tree[i][j])
print(ans)