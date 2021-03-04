N = int(input())
d = (7+N)%10-1
if d == -1:
    d=9
s = (N+10)%12-2
if s == -1:
    s = 11
elif s == -2:
    s = 10
print(chr(65+s)+str(d))