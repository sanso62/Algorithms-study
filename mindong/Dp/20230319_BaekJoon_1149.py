n=int(input())
rgb=[]
for _ in range(n):
    rgb.append(list(map(int, input().split())))

dp=rgb[0]
for i in range(1, n):
    dp[0],dp[1],dp[2]=rgb[i][0]+min(dp[1], dp[2]),rgb[i][1]+min(dp[2], dp[0]),rgb[i][2]+min(dp[0], dp[1])

print(min(dp))