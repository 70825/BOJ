from heapq import *
input=__import__('sys').stdin.readline
n=int(input())
D=sorted([[*map(int,input().split())] for _ in range(n)])
Room=[]
for i in range(n):
    if len(Room)>0 and Room[0]<=D[i][0]:heappop(Room)
    heappush(Room,D[i][1])
print(len(Room))