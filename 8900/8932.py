for i in range(int(input())):
    P=[*map(int,input().split())]
    t=[0,3,6];f=[1,2,4,5]
    A=[9.23076,1.84523,56.0211,4.99087,0.188807,15.9803,0.11193]
    B=[26.7,75,1.5,42.5,210,3.8,254]
    C=[1.835,1.348,1.05,1.81,1.41,1.04,1.88]
    ans=0
    for j in range(7):
        if j in t:ans+=int(A[j]*(B[j]-P[j])**C[j])
        else:ans+=int(A[j]*(P[j]-B[j])**C[j])
    print(ans)