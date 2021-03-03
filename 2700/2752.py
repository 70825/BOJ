B = [0] * 3
a,b,c = input().split()
B[0] = int(a)
B[1] = int(b)
B[2] = int(c)
if min(B) >= 1 and max(B) <=1000000 and len(set(B)) == 3:
    B.sort()
    print(B[0],B[1],B[2])