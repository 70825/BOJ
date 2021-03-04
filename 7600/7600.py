while 1:
    A=str(input())
    if A=='#':break
    B=A.lower();D=[0]*26
    for i in range(len(B)):
        if 97<=ord(B[i])<=122:D[ord(B[i])-97]+=1
    print(26-D.count(0))