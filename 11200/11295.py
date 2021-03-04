k=1
while 1:
    L=int(input())
    if L==0:break
    N=int(input())
    memo=[]
    for i in range(N):memo.append(int(input()))
    print('User',k)
    for i in memo:print("{0:.5f}".format(L*i/100000))
    k+=1