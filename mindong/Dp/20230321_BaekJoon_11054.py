n=int(input())
A=list(map(int, input().split()))

dp=[[A[0],1,1]]
for i in range(1,n):
    is_needed=True
    len_dp=len(dp)
    max_upcase, max_downcase=0,0
    for j in range(len_dp):
        if dp[j][0]<A[i] and dp[j][2]==1:
            if max_upcase<dp[j][1]:
                max_upcase=dp[j][1]
        elif dp[j][0]>A[i]:
            if max_downcase<dp[j][1]:
                max_downcase=dp[j][1]
    
    if max_downcase==0:
        dp.append([A[i],max_upcase+1, 1])
    else:
        dp.append([A[i],max_upcase+1, 1])
        dp.append([A[i],max_downcase+1, 0])
    # print()
    # print(dp)

print(max([v[1] for v in dp]))  