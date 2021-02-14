def Num(x):
    ans=0
    for i in range(len(x)):
        if 48<=ord(x[i])<58:
            ans+=ord(x[i])-48
    return ans
D=[]
for i in range(int(input())):
    D.append(input())
print('\n'.join(map(str,sorted(D,key= lambda a:[len(a),Num(a),a]))))