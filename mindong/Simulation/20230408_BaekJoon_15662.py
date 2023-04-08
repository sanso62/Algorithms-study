import sys
import collections
inputs=sys.stdin.read().splitlines()
t=int(inputs[0])
wheels=[0]
for w in inputs[1:t+1]:
    wheels.append(collections.deque(map(int, w)))
k=inputs[t+1]
operations=[]
for s in inputs[t+2:]:
    operations.append(list(map(int, s.split())))

def left_spin(num, dir):
    global wheels
    if wheels[num][2] != wheels[num+1][-2]:
        if num-1>0:
            left_spin(num-1, dir*-1)
        if dir==1:
            wheels[num].appendleft(wheels[num].pop())
        elif dir==-1:
            wheels[num].append(wheels[num].popleft())


def right_spin(num, dir):
    global wheels
    if wheels[num][-2] != wheels[num-1][2]:
        if num+1<=t:
            right_spin(num+1, dir*-1)
        if dir==1:
            wheels[num].appendleft(wheels[num].pop())
        elif dir==-1:
            wheels[num].append(wheels[num].popleft())
    

for op in operations:
    if op[0]-1>0:
        left_spin(op[0]-1, op[1]*-1)
    if op[0]+1<=t:
        right_spin(op[0]+1, op[1]*-1)
    if op[1]==1:
        wheels[op[0]].appendleft(wheels[op[0]].pop())
    elif op[1]==-1:
        wheels[op[0]].append(wheels[op[0]].popleft())
    # print(wheels)

ans=0
for wheel in wheels[1:]:
    if wheel[0]==1:
        ans+=1
print(ans)

