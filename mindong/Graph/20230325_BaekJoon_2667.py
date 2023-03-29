#bfs
import sys
import collections
inputs=sys.stdin.read().splitlines()
n=int(inputs[0])
cor=[]
for s in inputs[1:]:
    cor.append(list(map(int, s)))

result=[]
for i in range(n):
    for j in range(n):
        if cor[i][j]==1:
            q=collections.deque()
            q.append([i,j])
            cor[i][j]=0
            size=0
            while len(q)>0:
                # print(q)
                x,y=q.popleft()
                size+=1
                if x-1>=0 and cor[x-1][y]==1: 
                    q.append([x-1, y])
                    cor[x-1][y]=0
                if x+1<n and cor[x+1][y]==1: 
                    q.append([x+1, y])
                    cor[x+1][y]=0
                if y-1>=0 and cor[x][y-1]==1: 
                    q.append([x, y-1])
                    cor[x][y-1]=0
                if y+1<n and cor[x][y+1]==1: 
                    q.append([x, y+1])
                    cor[x][y+1]=0
            result.append(size)

print(len(result))
for r in sorted(result):
    print(r)
                
# #dfs
# import sys
# inputs=sys.stdin.read().splitlines()
# n=int(inputs[0])
# cor=[]
# for s in inputs[1:]:
#     cor.append(list(map(int, s)))

# def dfs(x,y):
#     global cor
#     global size
#     cor[x][y]=0
#     li=[]
#     if x-1>=0: li.append([x-1,y])
#     if x+1<n: li.append([x+1,y])
#     if y-1>=0: li.append([x, y-1])
#     if y+1<n: li.append([x, y+1])
#     for a,b in li:
#         if cor[a][b]==1:
#             size+=1
#             dfs(a,b)

# result=[]
# for i in range(n):
#     for j in range(n):
#         if cor[i][j]==1:
#             size=1
#             dfs(i,j)
#             result.append(size)

# print(len(result))
# for r in sorted(result):
#     print(r)