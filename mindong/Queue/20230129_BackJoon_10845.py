q=[]
result=[]
n=int(input())
for _ in range(n):
    op=input().split()
    if op[0]=="push":
        q.append(int(op[1]))
    elif op[0]=="pop":
        if len(q)==0:
            result.append(-1)
        else:
            result.append(q.pop(0))
    elif op[0]=="size":
        result.append(len(q))
    elif op[0]=="empty":
        if len(q)==0:
            result.append(1)
        else:
            result.append(0)
    elif op[0]=="front":
        if len(q)==0:
            result.append(-1)
        else:
            result.append(q[0])
    elif op[0]=="back":
        if len(q)==0:
            result.append(-1)
        else:
            result.append(q[-1])

for r in result:
    print(r)
