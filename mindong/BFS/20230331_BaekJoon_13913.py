#bfs
import collections
n, k=map(int, input().split())

checked=[-1 for _ in range(100001)]
depth=[0 for _ in range(100001)]
q=collections.deque()
q.append(n)
checked[n]=n
while len(q)>0:
    x=q.popleft()
    d=depth[x]
    # print(x, d)
    if x==k:
        break
    if x-1>=0 and checked[x-1]==-1:
        q.append(x-1)
        checked[x-1]=x
        depth[x-1]=d+1
    if x+1<=100000 and checked[x+1]==-1:
        q.append(x+1)
        checked[x+1]=x
        depth[x+1]=d+1
    if x*2<=100000 and checked[x*2]==-1:
        q.append(x*2)
        checked[x*2]=x
        depth[x*2]=d+1

ans=str(x)
while checked[x]!=x:
    x=checked[x]
    ans=str(x)+" "+ans
print(d)
print(ans)