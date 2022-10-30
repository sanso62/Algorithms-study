targets=list(map(int, input().split()))

e,s,m=0,0,0
year=0
while True:
    e, s, m = e+1, s+1, m+1
    year+=1
    if e<1 or e>15:
        e=1
    if s<1 or s>28:
        s=1
    if m<1 or m>19:
        m=1
    
    if [e,s,m]==targets:
        print(year)
        break
