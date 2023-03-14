n=int(input())
P=list(map(int, input().split()))

if n==1:
    print(P[0])
else:
    dp=[P[0], min(P[0]+P[0], P[1])]
    for i in range(2,n):
        # print(i, dp)
        li=[dp[i-j-1]+P[j] for j in range(i)]+[P[i]]
        dp.append(min(li))
        
    print(dp[-1])
