for i in range(int(input())):
    N=int(input());a=[0]*1000
    for j in range(N):b=int(input());a[b-1]+=1
    for j in range(1000):
        if max(a)==a[j]:print(j+1);break