input=__import__('sys').stdin.readline
for i in range(int(input())):
    a,b,c=map(int,input().split())
    print(min((a+c)**2+b**2,a**2+(b+c)**2,c**2+(a+b)**2))