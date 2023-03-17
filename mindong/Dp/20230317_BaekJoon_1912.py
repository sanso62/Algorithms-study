n=int(input())
li=list(map(int, input().split()))

dp=[li[0]]
for i in range(1,n):
    # print(dp)
    if li[i]<dp[i-1]+li[i]:
        dp.append(dp[i-1]+li[i])
    else:
        dp.append(li[i])

print(max(dp))