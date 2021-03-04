T=int(input())
for i in range(T):
    N,D,A,B,F=map(float,input().split())
    print(int(N),"{0:.2f}".format(D/(A+B)*F))