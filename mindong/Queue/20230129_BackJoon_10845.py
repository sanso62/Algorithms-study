q=[0 for _ in range(10001)]
result=[]
n=int(input())
begin, end=0,0
for _ in range(n):
    # print(begin, end)
    command=input().split()
    if command[0]=="push":
        if begin==0:
            begin+=1
            end+=2
            q[end-1]=int(command[1])
        else:
            q[end]=int(command[1])
            end+=1
    elif command[0]=="pop":
        if end-begin==0:
            result.append(-1)
        else:
            result.append(q[begin])
            q[begin]=0
            begin+=1
    elif command[0]=="size":
        result.append(end-begin)
    elif command[0]=="empty":
        if end-begin==0:
            result.append(1)
        else:
            result.append(0)
    elif command[0]=="front":
        if end-begin==0:
            result.append(-1)
        else:
            result.append(q[begin])
    elif command[0]=="back":
        if end-begin==0:
            result.append(-1)
        else:
            result.append(q[end-1])

for r in result:
    print(r)
