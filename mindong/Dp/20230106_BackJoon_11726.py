n=int(input())
sums=[1, 2]
for i in range(3, n+1):
    sums.append(sums[i-2]+sums[i-3])
if n==1:
    print(sums[0]%1007)
else:
    print(sums[-1]%10007)