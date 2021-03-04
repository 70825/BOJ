import math
A,P=map(int,input().split())
R,Q=map(int,input().split())
print('Slice of pizza' if A/P>math.pi*(R**2)/Q else 'Whole pizza')