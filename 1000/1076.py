A = input()
B = input()
C = input()
D = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
for i in range(10):
    if A == D[i]:
        A = str(i)
for i in range(10):
    if B == D[i]:
        B = str(i)
for i in range(10):
    if C == D[i]:
        C = int(i)
print(int(A+B)*10**C)