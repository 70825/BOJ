S=str(input())
D=['P','E','R']
k=0
for i in range(len(S)):
    if S[i]!=D[i%3]:k+=1
print(k)