input = __import__('sys').stdin.readline

n = int(input())
arr = [input().strip().split() for _ in range(n)]
stack = []
front = __import__('collections').deque()
sort_list = []
for i in range(n):
    for j in range(5):
        sort_list.append(arr[i][j])
        front.append(arr[i][j])
sort_list.sort(key= lambda x: [x[0], int(x[2:])])
idx = 0
while front:
    if len(stack) and stack[-1] == sort_list[idx]:
        stack.pop()
        idx += 1
    else: stack.append(front.popleft())
while stack:
    if len(stack) and stack[-1] == sort_list[idx]:
        stack.pop()
        idx += 1
    else:
        print('BAD')
        exit()
print('GOOD')