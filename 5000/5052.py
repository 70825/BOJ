input=lambda:__import__('sys').stdin.readline().strip()
def go(G):
    G.sort()
    for i in range(len(G)-1):
        if G[i]==G[i+1][0:len(G[i])]:return 'NO'
    return 'YES'
for _ in range(int(input())):
    n=int(input())
    D=[]
    for i in range(n):
        D.append(input())
    print(go(D))