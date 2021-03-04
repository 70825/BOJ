A,B=map(int,input().split())
if B>0:print(A//B);print(A%B)
else:C=A//abs(B);D=A-C*abs(B);C=-C;print(C);print(D)