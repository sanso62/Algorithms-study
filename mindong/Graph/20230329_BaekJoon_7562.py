#bfs
import collections
t=int(input())
result=[]
for _ in range(t):
    I=int(input())
    start_x, start_y=map(int, input().split())
    target_x, target_y=map(int, input().split())

    cnt=[[0]*I for _ in range(I)]
    q=collections.deque()
    q.append([start_x, start_y, 0])
    while len(q)>0:
        x,y,depth=q.popleft()
        if x==target_x and y==target_y:
            break
        xy=[[x-1, y-2], [x-2,y-1], [x-1,y+2], [x-2,y+1], [x+2,y-1],[x+1,y-2], [x+1,y+2],[x+2,y+1]]
        for i, j in xy:
            if (0<=i<I) and (0<=j<I):
                if cnt[i][j]==0:
                    q.append([i,j,depth+1])
                    cnt[i][j]=1

    result.append(depth)

for a in result:
    print(a)

    