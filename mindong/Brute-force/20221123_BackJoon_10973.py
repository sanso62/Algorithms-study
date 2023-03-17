n=int(input())
li=input().split()

if list(map(str,range(1,n+1)))==li:
    print("-1")
else:
    for i in range(-2,-n-1,-1):
        if int(li[i])>int(li[i+1]):
            l=[]
            changed=False
            for j in range(-1, i,-1):
                if int(li[j])<int(li[i]) and changed==False:
                    li[i], li[j]=li[j], li[i]
                    changed=True
                l.append(li[j])
            # print(li[:i+1]+l)
            ans=li[:i+1]+l
            print(" ".join(ans))

            break
