import sys
import collections
inputs=sys.stdin.read().splitlines()
n,m,R=map(int, inputs[0].split())
cnt=[]
for s in inputs[1:]:
    cnt.append(list(map(int,s.split())))

arr=[[0]*m for _ in range(n)]


start_r,start_c=0,0
end_r,end_c=n,m
lists=[]
while start_r<n/2 and start_c<m/2:
    x, y=start_r, start_c
    li=[]
    for i in range(start_r,end_r-1):
        li.append(cnt[i][y])
    x=end_r-1
    for j in range(start_c,end_c-1):
        li.append(cnt[x][j])
    y=end_c-1
    for i in range(end_r-1,start_r,-1):
        li.append(cnt[i][y])
    x=start_r
    for j in range(end_c-1,start_c,-1):
        li.append(cnt[x][j])
    lists.append(li)
    start_r+=1
    start_c+=1
    end_r-=1
    end_c-=1

for i in range(len(lists)):
    r=R%len(lists[i])
    lists[i]=lists[i][-r:]+lists[i][:-r]

result=[[0]*m for _ in range(n)]
start_r,start_c=0,0
end_r,end_c=n,m
for l in lists:
    for j in range(start_c+1,end_c):
        result[start_r][j]=str(l.pop())
    for i in range(start_r+1,end_r):
        result[i][end_c-1]=str(l.pop())
    for j in range(end_c-2,start_c-1,-1):
        result[end_r-1][j]=str(l.pop())
    for i in range(end_r-2,start_r-1,-1):
        result[i][start_c]=str(l.pop())
    start_r+=1
    start_c+=1
    end_r-=1
    end_c-=1

for r in result:
    print(" ".join(r))