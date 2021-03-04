input=__import__('sys').stdin.readline
input()
D=[*map(int,input().split())]
ans=sum(D)//2
for i in range(len(D)):
    if D[i]==ans:D.pop(i);break
print(' '.join(map(str,D)),ans)