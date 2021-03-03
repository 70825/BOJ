import sys
N,P=map(int,input().split());s=0
D=[[] for i in range(6)]
for i in range(N):
    A,B=map(int,sys.stdin.readline().split())
    if len(D[A-1])==0:D[A-1].insert(0,B);s+=1
    else:
        if D[A-1][0]>B:
            while 1:
                del D[A-1][0]
                s+=1
                if len(D[A-1])==0:break
                if (D[A-1][0])<=B:break
            if len(D[A-1])==0 or D[A-1][0]<B:D[A-1].insert(0,B);s+=1
        elif D[A-1][0]<B:D[A-1].insert(0,B);s+=1
print(s)