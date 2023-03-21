n=int(input())
dp=[0,1,1,0,0,1]
for i in range(1, n):
    dp[0], dp[1], dp[2], dp[3], dp[4], dp[5]=dp[1]+dp[2]+dp[5], dp[0]+dp[3], dp[0]+dp[4], dp[1], dp[2], dp[0]
print(dp[0])