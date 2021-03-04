N=input()
L,R,A=N.split()
L=int(L)
R=int(R)
A=int(A)
if 0<=L<=100 and 0<=R<=100 and 0<=A<=100:
    while A>0:
        if L>R:
            R += 1
            A -= 1
        elif L<R:
            L += 1
            A -= 1
        elif L == R and A >= 2:
            L += 1
            A -= 1
        else:
            break
    if L<=R:
        print(2*L)
    else:
        print(2*R)