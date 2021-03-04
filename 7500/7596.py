d=1
while 1:
    A=int(input())
    if A==0:break
    D=[]
    for i in range(A):D.append(str(input()))
    D.sort()
    print(d)
    for i in range(A):print(D[i])
    d+=1