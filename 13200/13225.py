T=int(input())
for i in range(T):
    d=0;A=int(input())
    for i in range(A):
        if A/(i+1)==A//(i+1):
            d+=1
    print(A,d)