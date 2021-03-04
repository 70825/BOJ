from decimal import Decimal
D=[]
for i in range(int(input())):
    D.append(Decimal(input()))
D.sort()
print("{0:.6f}".format(sum(D)/len(D)))
if len(D)%2==1:
    print("{0:.6f}".format(D[len(D)//2]))
else:
    K=(D[len(D)//2]+D[len(D)//2-1])/2
    print("{0:.6f}".format(K))