n, m=list(map(int, input().split()))

for num in range(n,m+1):
    is_pn=True
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            is_pn=False
            break
    
    if num==1:
        is_pn=False 
    if num==2 or num==3:
        is_pn=True
    if is_pn:
        print(num)