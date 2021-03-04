A,B=map(int,input().split())
if A != B:
    print(abs(B-A)-1)
else:
    print(0)
if A<=B:
    for i in range(A+1,B):
        print(i,end=" ")
else:
    for i in range(B+1,A):
        print(i,end=" ")