from collections import Counter
n=int(input())
k=input()
a,b=Counter(k)['2'],Counter(k)['e']
print(2) if a>b else print('e') if b>a else print('yee')