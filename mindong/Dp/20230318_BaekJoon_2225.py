n, k = map(int, input().split())
DIVMOD=1000000000
dp=[[1 for _ in range(k-1)]]+[[1] for _ in range(1,n+1)]
# print(dp)
for i in range(1,n+1):
    for j in range(2, k):
        dp[i].append(sum([dp[l][j-2]%DIVMOD for l in range(i+1)])%DIVMOD)
# print(dp)
if k==1:
    print(1)
else:
    print(sum([dp[m][k-2]%DIVMOD for m in range(n+1)])%DIVMOD)