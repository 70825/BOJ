A = str(input())
K = ["c=","c-","d-","lj",'nj','s=','z=','dz=']
d = 0;s = 0
while d < len(A):
    if d <= len(A)-3 and A[d]+A[d+1]+A[d+2] in K: d+=3
    elif d <= len(A)-2 and A[d]+A[d+1] in K:d += 2
    else:d += 1
    s += 1
print(s)