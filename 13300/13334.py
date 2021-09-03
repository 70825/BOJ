from heapq import *
input = __import__('sys').stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(sorted([*map(int, input().split())]))
d = int(input())

ans = 0
arr.sort(key=lambda x: [x[1], x[0]])
people = []
for i in range(n):
    if arr[i][1] - arr[i][0] <= d:
        while people:
            person = heappop(people)
            if arr[i][1] - person[0] <= d:
                heappush(people, person)
                break
        heappush(people, arr[i])
        ans = max(ans, len(people))
print(ans)