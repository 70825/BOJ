memo=['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for i in range(int(input())):
    S=str(input())
    count=[0]*8
    for j in range(38):
        for k in range(8):
            if S[j]+S[j+1]+S[j+2]==memo[k]:
                count[k]+=1
    print(' '.join(map(str,count)))