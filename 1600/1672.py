input()
S=[*input()]
for i in range(len(S)-1,0,-1):
    if S[i-1]==S[i]:continue
    elif S[i]+S[i-1] in 'AGA':S[i-1]='C'
    elif S[i]+S[i-1] in 'ACA':S[i-1]='A'
    elif S[i]+S[i-1] in 'ATA':S[i-1]='G'
    elif S[i]+S[i-1] in 'CGC':S[i-1]='T'
    elif S[i]+S[i-1] in 'GTG':S[i-1]='A'
    else:S[i-1]='G'
print(S[0])