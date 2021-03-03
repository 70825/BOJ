A,B,C=map(int,input().split())
i,j,k=map(int,input().split())
l=min(A/i,B/j,C/k)
print(A-i*l,B-j*l,C-k*l)