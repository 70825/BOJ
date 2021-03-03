A,B=map(int,input().split())
C=min(A,B)-1;D=max(A,B)
print(D*(D+1)//2-C*(C+1)//2)