N=int(input())
D=[]
while N//9!=0:
    D.append(N%9)
    N=N//9
print(N%9,end="")
for i in range(len(D)):
    print(D[len(D)-1-i],end="")