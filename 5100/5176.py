for i in range(int(input())):
    p,m=map(int,input().split());D=[];k=0
    for j in range(p):
        n=int(input())
        if D.count(n)==0:D.append(n)
        else:k+=1
    print(k)