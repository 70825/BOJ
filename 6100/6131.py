N=int(input())
k=0
for i in range(1,1000):
    for j in range(i,1001):
        if i**2+N==j**2:
            k+=1
print(k)