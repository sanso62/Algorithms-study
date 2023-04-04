import collections
n=int(input())
inputs=list(map(int, input().split()))
deque=collections.deque()
for i,v in enumerate(inputs):
    deque.append([i+1,v])
count=len(deque)
i=0
while count>0:
    next,deque[i][1]=deque[i][1],0
    print(deque[i][0], end=" ")
    # print(deque,i,next)
    if count==1:
        break
    while next>0:
        if i+1>=len(deque):
            deque.append(deque.popleft())
            i-=1
            continue
        if deque[i+1][1]==0:
            i+=1
        else:
            i+=1
            next-=1
    while next<0:
        if i-1<0:
            deque.appendleft(deque.pop())
            i+=1    
        if deque[i-1][1]==0:
            i-=1
        else:
            i-=1
            next+=1
    count-=1


                