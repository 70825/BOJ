sub_memo=[['1','Q','A','Z','`'],['2','W','S','X'],['3','E','D','C'],
          ['4','5','R','T','F','G','V','B'],['6','7','Y','U','H','J','N','M'],
          ['8','I','K',','],['9','O','L','.'],['0','-','=','P','[',']',';','\'','/']]
memo=[0,0,0,0,0,0,0,0]
N=str(input())
for i in range(len(N)):
    for k in range(8):
        if N[i] in sub_memo[k]:
            memo[k]+=1
            break
for i in memo:
    print(i)