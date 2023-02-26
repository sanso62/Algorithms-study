deque=[]
result=[]
n=int(input())
for _ in range(n):
    op=input().split()
    if op[0]=="push_front":
        deque=[int(op[1])]+deque
    if op[0]=="push_back":
        deque.append(int(op[1]))
    elif op[0]=="pop_front":
        if len(deque)==0:
            result.append(-1)
        else:
            result.append(deque.pop(0))
    elif op[0]=="pop_back":
        if len(deque)==0:
            result.append(-1)
        else:
            result.append(deque.pop())
    elif op[0]=="size":
        result.append(len(deque))
    elif op[0]=="empty":
        if len(deque)==0:
            result.append(1)
        else:
            result.append(0)
    elif op[0]=="front":
        if len(deque)==0:
            result.append(-1)
        else:
            result.append(deque[0])
    elif op[0]=="back":
        if len(deque)==0:
            result.append(-1)
        else:
            result.append(deque[-1])

for r in result:
    print(r)
