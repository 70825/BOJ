def X(a,b):
    P = a * b
    return P
def Y(b,c,d,e):
    if c >= e:
        return b
    else:
        B = b + d*(e-c)
        return B
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(min(X(a,e),Y(b,c,d,e)))