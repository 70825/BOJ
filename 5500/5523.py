input =__import__('sys').stdin.readline
x,y=0,0
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:x+=1
    if b>a:y+=1
print(x,y)