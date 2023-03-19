n=int(input())
B=10007
dp=[1 for _ in range(10)]
for _ in range(1, n):
    cur_dp=dp[::]
    for i in range(10):
        dp[i]=sum(cur_dp[:i+1])%B
    # print(dp)

print(sum(dp)%B)