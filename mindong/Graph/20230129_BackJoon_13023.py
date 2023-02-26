n,m = map(int, input().split())
graph=[[] for _ in range(n)]
ans=0
for _ in range(m):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def next(num, li):
    global ans
    if num==5:
        ans=1
        return 1
    else:
        for k in graph[li[-1]]:
            if k not in li:
                next(num+1, li+[k])

for i in range(n):
    li=[i]
    for j in graph[i]:
        next(2, li+[j])
        if ans==1:
            break
    if ans==1:
        break

print(ans)

    