B=input().split()
C=[0,0,0,0,0]
for i in range(5):
    C[i] = int(B[i])
while C[0]!=1 or C[1]!=2 or C[2]!=3 or C[3]!=4 or C[4]!=5:
    for i in range(4):
        if C[i] > C[i+1]:
            temp=C[i]
            C[i]=C[i+1]
            C[i+1]=temp
            print(C[0],C[1],C[2],C[3],C[4])