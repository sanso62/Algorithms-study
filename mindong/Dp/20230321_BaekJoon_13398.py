n=int(input())
arr=list(map(int, input().split()))

left_dp=[arr[0]]
for i in range(1,n-1):
    left=max(left_dp[0], arr[i-1])
    right=max(left_dp[0], arr[i+1])

