n=int(input())
wine=[]
for _ in range(n):
    wine.append(int(input()))
if n==1:
    print(wine[0])
elif n==2:
    print(wine[0]+wine[1])
else:
    dp=[[wine[0]+wine[1],2], [wine[0]+wine[2],1], [wine[1]+wine[2],0]]
    # print(dp)
    for i in range(3, n):
        no_next_i, no_next_value=0,[]
        for j in range(3):
            if dp[j][1]==2:
                no_next_value.append(dp[j][0])
                dp[j][0]+=wine[i]
                dp[j][1]-=1
            elif dp[j][1]==1:   
                no_next_value.append(dp[j][0])
                dp[j][0]+=wine[i]
                dp[j][1]-=1
            elif dp[j][1]==0:
                no_next_value.append(dp[j][0])
                no_next_i=j

        dp[no_next_i][0]=max(no_next_value)
        dp[no_next_i][1]=2
        # print(dp)

    print(max([v[0] for v in dp]))