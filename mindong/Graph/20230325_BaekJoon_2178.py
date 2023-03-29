#bfs
import sys
import collections
inputs=sys.stdin.read().splitlines()
n, m=map(int, inputs[0].split())
cnt=[]
for input in inputs[1:]:
    cnt.append(list(map(int, input)))

q=collections.deque()
q.append([1,1,1])
cnt[0][0]=0
while len(q)>0:
    x,y,depth=q.popleft()
    # print(x,y,depth)
    if x==n and y==m:
        break
    if x+1<=n and cnt[x][y-1]==1:
        q.append([x+1,y,depth+1])
        cnt[x][y-1]=0
    if y+1<=m and cnt[x-1][y]==1:
        q.append([x, y+1,depth+1])
        cnt[x-1][y]=0
    if x-1>0 and cnt[x-2][y-1]==1:
        q.append([x-1, y,depth+1])
        cnt[x-2][y-1]=0
    if y-1>0 and cnt[x-1][y-2]==1:
        q.append([x, y-1,depth+1])
        cnt[x-1][y-2]=0
# print(q)
print(depth)
    




# #dfs -> No way...
# import sys
# inputs=sys.stdin.read().splitlines()
# n, m=map(int, inputs[0].split())
# cnt=[]
# for input in inputs[1:]:
#     cnt.append(list(map(int, input)))

# min=10000
# def dfs(x,y,l):
#     global min
#     # print(x,y, n, m)
#     if x==n and y==m:
#         if min>l:
#             min=l
#         if min<n+m:
#             return True
#         else:
#             return False
#     li=[]
#     if x+1<=n and cnt[x-1+1][y-1]==1:
#         cnt[x-1+1][y-1]=0
#         if dfs(x+1,y,l+1):
#             return True
#         cnt[x-1+1][y-1]=1
#     if y+1<=m and cnt[x-1][y-1+1]==1:
#         cnt[x-1][y-1+1]=0
#         if dfs(x,y+1,l+1):
#             return True
#         cnt[x-1][y-1+1]=1
#     if x-1>0 and cnt[x-1-1][y-1]==1:
#         cnt[x-1-1][y-1]=0
#         if dfs(x-1,y,l+1):
#             return True
#         cnt[x-1-1][y-1]=1
#     if y-1>0 and cnt[x-1][y-1-1]==1:
#         cnt[x-1][y-1-1]=0
#         if dfs(x,y-1,l+1):
#             return True
#         cnt[x-1][y-1-1]=1
    
# cnt[0][0]=0
# dfs(1,1,1)
# print(min)