n=int(input())
li=list(map(str,range(1, n+1)))
last=li[::-1]

def factorial(val):
    if val==1:
        return val
    else:
        return val*factorial(val-1)
    
n_factorial=factorial(n)
# print(n_factorial)
for _ in range(n_factorial):
    print(" ".join(li))
    for i in range(-2,-n-1,-1):
        if int(li[i])<int(li[i+1]):
            l=[]
            changed=False
            for j in range(-1, i,-1):
                if int(li[j])>int(li[i]) and changed==False:
                    li[i], li[j]=li[j], li[i]
                    changed=True
                l.append(li[j])
            li=li[:i+1]+l
            break
