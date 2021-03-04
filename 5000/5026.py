for i in range(int(input())):
 S=str(input())
 if S=='P=NP':print('skipped')
 else:A,B=map(int,S.split('+'));print(A+B)