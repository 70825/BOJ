from collections import deque
n, e = map(int,input().split())
start = 1
graph = {}
for i in range(1,n+1):
    graph[i]={}
for _ in range(e):
    v1, v2, l = map(int,input().split())
    graph[v1][v2]=l
    graph[v2][v1]=l
v1, v2 = map(int,input().split())

def dijkstra(y,z):
    distance = [float('inf')]*(n+1)
    distance[y]=0
    q=deque([[0,y]])
    while q:
        t, x = q.popleft()
        for nx in graph[x].keys():
            if distance[nx]>t+graph[x][nx]:
                distance[nx]=graph[x][nx]+t
                q.append([graph[x][nx]+t,nx])
    return distance[z]


route1 = dijkstra(start,v1) + dijkstra(v1,v2) + dijkstra(v2,n)
route2 = dijkstra(start,v2) + dijkstra(v2,v1) + dijkstra(v1,n)
dis = min(route1, route2)
print(dis if dis < 1000000000 else '-1')