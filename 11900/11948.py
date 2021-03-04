A=[0]*4;d=0;B=[0]*2
for i in range(4):A[i]=int(input());d+=A[i]
for i in range(2):B[i]=int(input());d+=B[i]
print(d-min(A)-min(B))