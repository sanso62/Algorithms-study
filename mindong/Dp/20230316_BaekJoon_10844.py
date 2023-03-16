n=int(input())
dp=[0,1,1,1,1,1,1,1,1,1]

for _ in range(1,n):
    cur=dp[::]
    for i in range(10):
        if i==0:
            dp[i]=cur[i+1]%1000000000
        elif i==9:
            dp[i]=cur[i-1]%1000000000
        else:
            dp[i]=cur[i-1]%1000000000+cur[i+1]%1000000000

print(sum(dp)%1000000000)