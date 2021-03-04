for i in range(int(input())):
    n,m=map(int,input().split());k=0
    for j in range(n,m+1):k+=str(j).count('0')
    print(k)