NO='''|>___/|     /}
| O O |    / }
( =0= )""""  \\
| ^  ____    |
|_|_/    ||__|'''
YES='''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|'''
n,m=map(int,input().split())
D=[[*map(int,input().split())] for _ in range(m)]
K=[[*map(int,input().split())] for _ in range(n)]
err=0
for i in range(n):
    for j in range(m):
        if D[m-j-1][i]!=K[i][j]:err=1
if err==0:print(YES)
else:print(NO)