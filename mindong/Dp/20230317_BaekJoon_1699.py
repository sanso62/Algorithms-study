n=int(input())

dp=[1]
for num in range(2, n+1):
    if int((num-1)**0.5)+1==num**0.5:
        dp.append(1)
    else:
        i, j=num-2, 0
        min_count=num+1
        while i>j:
            if min_count>(dp[i]+dp[j]):
                min_count=dp[i]+dp[j]
            i-=1
            j+=1
        dp.append(min_count)

print(dp[-1])