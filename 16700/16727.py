p1,s1=map(int,input().split())
s2,p2=map(int,input().split())
p=p1+p2;s=s1+s2
print('Persepolis' if p>s or (p==s and p2>s1) else ('Esteghlal' if s>p or (p==s and s1>p2) else 'Penalty'))