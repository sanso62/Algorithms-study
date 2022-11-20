# 9095번 - 1,2,3 더하기

dp = [0,1,2,4,0,0,0,0,0,0,0]

for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

n = int(input())

for _ in range(0,n):
    num = int(input())
    print(dp[num])
