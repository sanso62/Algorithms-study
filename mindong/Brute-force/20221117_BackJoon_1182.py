n, s=map(int, input().split())
li=list(map(int, input().split()))

if s==0:
    result=-1
else:
    result=0
def True_or_False(num, sum):
    global result
    if num==n:
        if sum==s:
            result+=1
        return
    True_or_False(num+1, sum+li[num])
    True_or_False(num+1, sum)

True_or_False(0, 0)
print(result)