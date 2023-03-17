n, m, b= map(int, input().split())
arr=[]
for _ in range(n):
    li=list(map(int, input().split()))
    arr+=li

arr.sort(reverse=True)
if arr[0]==arr[-1]:
    print(0,arr[0])
else:
    min_t=256*500*500*2+1
    height=0
    for h in range(257):
        t=0
        box=b
        is_possible=True
        for i in range(len(arr)):
            if h<arr[i]:
                t+=(arr[i]-h)*2
                box+=arr[i]-h
            elif h>arr[i]:
                if h-arr[i]>box:
                    is_possible=False
                    break
                else:
                    t+=h-arr[i]
                    box-=(h-arr[i])
            else:
                pass
        if is_possible and min_t>=t:
            min_t=t
            height=h

    print(min_t, height)        