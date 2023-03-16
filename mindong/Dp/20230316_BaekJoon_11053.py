n=int(input())
A=list(map(int, input().split()))

dp=[1]
for i in range(1,n):
    # print(dp)
    max_l=0
    for j in range(i):
        if A[j]<A[i]:
            if max_l<dp[j]:
                max_l=dp[j]
    
    if max_l==0:
        dp.append(1)
    else:
        dp.append(max_l+1)

print(max(dp))