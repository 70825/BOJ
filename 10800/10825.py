memo=[]
for i in range(int(input())):
    a,b,c,d=input().split()
    b=int(b);c=int(c);d=int(d)
    memo.append([-b,c,-d,a])
for i in sorted(memo):
    print(i[3])