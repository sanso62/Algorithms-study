t=int(input())
li_n=[]
DIVMOD=1000000009
for _ in range(t):
    li_n.append(int(input()))

dp=[1,2,4]
for i in range(3,max(li_n)):
    dp.append((dp[i-1]%DIVMOD+dp[i-2]%DIVMOD+dp[i-3]%DIVMOD)%DIVMOD)

for n in li_n:
    print(dp[n-1])