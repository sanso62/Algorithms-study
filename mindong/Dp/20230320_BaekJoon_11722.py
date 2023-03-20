n=int(input())
A=list(map(int, input().split()))

dp=[1]
for i in range(1,n):
    max_len=0
    for j in range(i):
        if A[j]>A[i]:
            if max_len<dp[j]:
                max_len=dp[j]
    dp.append(max_len+1)

print(max(dp))