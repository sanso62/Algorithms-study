n=int(input())

dp=[0,1]
for _ in range(1,n):
    dp[0],dp[1]=dp[0]+dp[1], dp[0]

print(dp[0]+dp[1])