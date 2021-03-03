P=str(input())
P=int(P,2)
P=oct(P)
for i in range(2,len(P)):
    print(P[i],end="")