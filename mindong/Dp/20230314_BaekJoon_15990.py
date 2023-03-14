t=int(input())
N=[]
for _ in range(t):
    N.append(int(input()))
init_N=N[::]
N.sort()

dp=[[1,0,0], [0,1,0], [1,1,1]]
for i in range(3, N[-1]):
    dp.append([(dp[i-1][1]+dp[i-1][2])%1000000009, (dp[i-2][0]+dp[i-2][2])%1000000009, (dp[i-3][0]+dp[i-3][1])%1000000009])

result=[]
for j in init_N:
    result.append(sum(dp[j-1])%1000000009)

for ans in result:
    print(ans)