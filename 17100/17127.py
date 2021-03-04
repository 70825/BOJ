n=int(input())
D=[*map(int,input().split())]
def mul(a,b):
    k=1
    for i in range(a,b):
        k*=D[i]
    return k
A = mul(0,len(D)-3)+D[-3]+D[-2]+D[-1]
B = D[0]+mul(1,len(D)-2)+D[-2]+D[-1]
C = D[0]+D[1]+mul(2,len(D)-1)+D[-1]
D = D[0]+D[1]+D[2]+mul(3,len(D))
print(max(A,B,C,D))