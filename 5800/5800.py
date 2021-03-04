for i in range(int(input())):
 A=list(map(int,input().split()));del A[0];A.sort();k=[0]*(len(A)-1)
 for j in range(len(k)):k[j]=A[j+1]-A[j]
 print('Class',i+1);print('Max',str(A[len(A)-1])+', Min',str(A[0])+', Largest gap',max(k))