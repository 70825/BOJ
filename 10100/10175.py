T=int(input())
for i in range(T):
    C=[0,0,0,0];d=0
    A,B=map(str,input().split())
    for j in range(len(B)):
        if B[j]=='B':C[0]+=2
        elif B[j]=='C':C[1]+=1
        elif B[j]=='M':C[2]+=4
        else:C[3]+=3
    print(A+':',end=" ")
    if C.count(max(C))>1:print('There is no dominant species')
    else:
        if max(C)==C[0]:print('The Bobcat',end=" ")
        elif max(C)==C[1]:print('The Coyote',end=" ")
        elif max(C)==C[2]:print('The Mountain Lion',end=" ")
        else:print('The Wolf',end=" ")
        print('is the dominant species')