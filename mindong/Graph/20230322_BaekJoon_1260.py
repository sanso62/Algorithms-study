import collections

n, m, v=map(int, input().split())
a_li=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a_li[a-1].append(b)
    a_li[b-1].append(a)
for i in range(n):
    a_li[i]=sorted(list(set(a_li[i])))

# print(a_li)

def dfs(v1):
    global dfs_checked
    dfs_checked[v1-1]=True
    print(v1, end=" ")
    for v2 in a_li[v1-1]:
        if not dfs_checked[v2-1]:
            dfs(v2)

dfs_checked=[False for _ in range(n)]
dfs(v)
print()

bfs_checked=[False for _ in range(n)]
bfs_checked[v-1]=True
q=collections.deque()
q.append(v)
bfs_ans=""
while len(q)>0:
    for vertex in a_li[q[0]-1]:
        if not bfs_checked[vertex-1]:
            q.append(vertex)
            bfs_checked[vertex-1]=True
    bfs_ans +=" "+str(q.popleft())
print(bfs_ans[1:])