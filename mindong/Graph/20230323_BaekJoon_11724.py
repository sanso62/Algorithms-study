#bfs
from collections import deque 
n, m= map(int, input().split())
a_li=[[] for _ in range(n)]
for _ in range(m):
    u, v=map(int, input().split())
    a_li[u-1].append(v)
    a_li[v-1].append(u)

# print(a_li)
checked=[False for _ in range(n)]
q=deque()
start_v=0
cc=0
checked_true=0
while checked_true<n:
    cc+=1
    checked[start_v]=True
    start_v+=1
    checked_true+=1
    q.append(start_v)
    while len(q)>0:
        # print(start_v,q)
        for vertex in a_li[q[0]-1]:
            if not checked[vertex-1]:
                checked[vertex-1]=True
                checked_true+=1
                q.append(vertex)
                if vertex==start_v+1:
                    start_v+=1
        q.popleft()

print(cc)


# dfs
# import sys
# sys.setrecursionlimit(1001)
# n, m= map(int, input().split())
# a_li=[[] for _ in range(n)]
# for _ in range(m):
#     u, v=map(int, input().split())
#     a_li[u-1].append(v)
#     a_li[v-1].append(u)

# def dfs(x):
#     global checked
#     checked[x-1]=True
#     for vertex in a_li[x-1]:
#         if not checked[vertex-1]:
#             dfs(vertex)

# checked=[False for _ in range(n)]
# cc=0
# for i in range(n):
#     if not checked[i]:
#         dfs(i+1)
#         cc+=1

# print(cc)
