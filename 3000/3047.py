D=[0]*3;D[0],D[1],D[2]=map(int,input().split());E=str(input());D.sort();A=D[0];B=D[1];C=D[2]
for i in range(3):
    if E[i]=='A':print(A,end=" ")
    elif E[i]=='B':print(B,end=" ")
    else:print(C,end=" ")