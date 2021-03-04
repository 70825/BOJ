D=[]
for i in range(int(input())):
    K=str(input())
    D.append(K)
    if K[::-1] in D:
        print(len(K),K[len(K)//2])