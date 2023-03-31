#bfs
import collections
s=int(input())

q=collections.deque()
q.append([1,1,1])
checked=[[False]*1001 for _ in range(1001)]
checked[1][1]=True

while len(q)>0:
    window,clip,depth=q.popleft()
    # print(window)
    if window==s:
        break

    if not checked[window][window]:
        q.append([window, window, depth+1])
        checked[window][window]=True
    if window+clip<=1000 and not checked[window+clip][clip]:
        q.append([window+clip, clip, depth+1])
        checked[window+clip][clip]=True
    if window-1>=0 and not checked[window-1][clip]:
        q.append([window-1, clip, depth+1])
        checked[window-1][clip]=True
        
print(depth)