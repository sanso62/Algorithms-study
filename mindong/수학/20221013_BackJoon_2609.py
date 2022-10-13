n, m = list(map(int, input().split()))
if n>m:
    n, m=m, n
    
def is_pn(x):
    if 1<x<4:
        return True
    for j in range(2,int(x**0.5)+1):
        if x%j==0:
            return False
    return True

greatest_common_factor, i=1, 2
while i<n+1:
    if n%i==0 and m%i==0 and is_pn(i):
        a, b=n,m
        while a%i==0 and b%i==0:
            greatest_common_factor*=i
            a//=i
            b//=i
    i+=1    

least_common_multiple=(n//greatest_common_factor)*m

print(greatest_common_factor)
print(least_common_multiple)