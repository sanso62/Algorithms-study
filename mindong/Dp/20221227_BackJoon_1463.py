n=int(input())
min_num=n
def next(q, num):
    # print(q,num)
    global min_num
    if q==1:
        if min_num>num:
            min_num=num
        return 0
    else:
        if min_num>num:
            if q%3==0:
                next(q//3, num+1)
            if q%2==0:
                next(q//2, num+1)
            next(q-1, num+1)
        else:
            return 0
next(n, 0)
print(min_num)