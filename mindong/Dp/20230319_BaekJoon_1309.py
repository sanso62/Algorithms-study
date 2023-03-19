n=int(input())
dp=[1,1,1]
B=9901
for i in range(1, n):
    dp[0], dp[1], dp[2]=(dp[0]+dp[1]+dp[2])%B, (dp[0]+dp[2])%B, (dp[0]+dp[1])%B

print(sum(dp)%B)