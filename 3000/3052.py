D=[]
for i in range(10):
    A=int(input())
    D.append(A%42)
print(len(list(set(D))))