A,B = map(int,input().split())
C = A*B
D = input()
E = D.split()
for i in range(5):
    print(int(E[i])-C,end=" ")