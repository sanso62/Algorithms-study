#bfs
import sys
import collections
inputs=sys.stdin.read().splitlines()
m,n=map(int, inputs[0].split())
cnt=[]
for input in inputs[1:]:
    cnt.append(list(map(int, input.split())))

cnt_red_tomatoes=collections.deque()
n_green_tomatoes=0
for i in range(n):
    for j in range(m):
        if cnt[i][j]==1:
            cnt_red_tomatoes.append([i+1,j+1,0])
        elif cnt[i][j]==0:
            n_green_tomatoes+=1

if n_green_tomatoes==0:
    print(0)
else:
    while len(cnt_red_tomatoes)>0:
        x,y,depth=cnt_red_tomatoes.popleft()
        if x-1>0 and cnt[x-2][y-1]==0:
            cnt_red_tomatoes.append([x-1,y,depth+1])
            cnt[x-2][y-1]=1
            n_green_tomatoes-=1
        if x+1<=n and cnt[x][y-1]==0:
            cnt_red_tomatoes.append([x+1,y,depth+1])
            cnt[x][y-1]=1
            n_green_tomatoes-=1
        if y-1>0 and cnt[x-1][y-2]==0:
            cnt_red_tomatoes.append([x,y-1,depth+1])
            cnt[x-1][y-2]=1
            n_green_tomatoes-=1
        if y+1<=m and cnt[x-1][y]==0:
            cnt_red_tomatoes.append([x,y+1,depth+1])
            cnt[x-1][y]=1
            n_green_tomatoes-=1

    if n_green_tomatoes==0:
        print(depth)
    else:
        print(-1)