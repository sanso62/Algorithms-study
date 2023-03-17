n=int(input())
A=list(map(int, input().split()))

dp=[1]
li=[[0]]
for i in range(1,n):
    # print(li)
    max_l=0
    max_j=0
    for j in range(i):
        if A[j]<A[i]:
            if max_l<dp[j]:
                max_l=dp[j]
                max_j=j

    if max_l==0:
        dp.append(1)
        li.append([i])
    else:
        dp.append(max_l+1)
        li.append(li[max_j]+[i])
    
print(max(dp))
result=[]
for k in max(li,key=len):
    result.append(str(A[k]))
print(" ".join(result))