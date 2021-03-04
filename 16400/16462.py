import decimal
decimal.getcontext().rounding=decimal.ROUND_HALF_UP
N=int(input())
memo=[0]*N
for i in range(N):
    S=str(input())
    S=S.replace('0','9')
    S=S.replace('6','9')
    if int(S)>=100:memo[i]=100
    else:memo[i]=int(S)
print(decimal.Decimal(str(sum(memo)/N)).to_integral_value())