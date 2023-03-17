n=int(input())
w=[]
for _ in range(n):
    l=list(map(int, input().split()))
    w.append(l)

indices=list(range(n))
min_cost=4000001
def choose_city(start, prev, li, cost, num):
    global min_cost
    if num==0:
        if w[prev][start]==0:
            return
        cost+=w[prev][start]
        if cost<min_cost:
            min_cost=cost
        return
    for i in range(num):
        if prev!=li[i] and w[prev][li[i]]==0:
            continue
        li[i],li[-1]=li[-1],li[i]
        cur=li.pop()
        if num<n:
            choose_city(start, cur, li, cost+w[prev][cur], num-1)
        else:
            choose_city(i, i, li, cost, num-1)
        li.append(cur)
        li[i],li[-1]=li[-1],li[i]

choose_city(0, 0, indices, 0, n)

print(min_cost)
