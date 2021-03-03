memo=[]
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a<=b<=c:memo.append('Ordered')
    elif a>=b>=c:memo.append('Ordered')
    else:memo.append('Unordered')
print('Gnomes:')
print('\n'.join(map(str,memo)))