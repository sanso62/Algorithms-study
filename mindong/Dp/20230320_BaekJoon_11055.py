n=int(input())
arr=list(map(int, input().split()))

dp=[arr[0]]
for i in range(1,n):
    max_sum=arr[i]
    for j in range(i):
        if arr[j]<arr[i]:
            if max_sum<dp[j]+arr[i]:
                max_sum=dp[j]+arr[i]
    dp.append(max_sum)
    # print(dp)

print(max(dp))         