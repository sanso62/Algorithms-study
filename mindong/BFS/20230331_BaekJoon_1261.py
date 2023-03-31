import sys
import collections

inputs=sys.stdin.read().splitlines()
m,n=map(int, inputs[0].split())
cnt=[]
for input in inputs[1:]:
    cnt.append(list(map(int, input)))

def dfs(a,b,d):
    global q
    global checked
    if a==n and b==m:
        print(d)
        return True
    if cnt[a-1][b-1]==1:
        q.append([a,b,d+1])
        cnt[a-1][b-1]=0
        return False
    if a-1>0 and not checked[a-1-1][b-1]:
        checked[a-1-1][b-1]=True
        if dfs(a-1,b,d):
            return True
    if a+1<=n and not checked[a+1-1][b-1]:
        checked[a+1-1][b-1]=True
        if dfs(a+1,b,d):
            return True
    if b-1>0 and not checked[a-1][b-1-1]:
        checked[a-1][b-1-1]=True
        if dfs(a,b-1,d):
            return True
    if b+1<=m and not checked[a-1][b+1-1]:
        checked[a-1][b+1-1]=True
        if dfs(a,b+1,d):
            return True
    
q=collections.deque()
q.append([1,1,0])
checked=[[False]*m for _ in range(n)]
checked[0][0]=True
done=False
while len(q)>0 and not done:
    # print(q)/
    x,y,depth=q.popleft()
    if x==n and y==m:
        print(depth)
        break
    done=dfs(x,y,depth)

    
    
