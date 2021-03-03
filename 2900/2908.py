A,B = map(int,input().split())
E = (A%10)*100 + (A%100-A%10) +(A//100)
F = (B%10)*100 + (B%100-B%10) +(B//100)
print(max(E,F))