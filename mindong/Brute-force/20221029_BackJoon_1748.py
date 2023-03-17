n=input()
m=len(n)
if m==1:
    result=int(n)
    print(result)
else:
    result=9
    for i in range(2, m):
        result+=(9*10**(i-1))*i
    result+=(int(n)-10**(m-1)+1)*(m)
    print(result)