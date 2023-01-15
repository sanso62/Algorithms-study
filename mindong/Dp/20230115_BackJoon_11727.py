n=int(input())
dp=[0, 1, 3]
for i in range(3, n+1):
    dp.append(dp[i-2]*2+dp[i-1])

if n<3:
    print(dp[n])
else:
    print(dp[n]%10007)