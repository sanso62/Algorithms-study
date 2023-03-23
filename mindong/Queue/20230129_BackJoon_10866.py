deque=[0 for _ in range(20002)]
result=[]
n=int(input())
begin, end=10000,10001
for _ in range(n):
    # print(begin, end)
    command=input().split()
    if command[0]=="push_back":
        deque[end]=int(command[1])
        end+=1
    elif command[0]=="push_front":
        deque[begin]=int(command[1])
        begin-=1
    elif command[0]=="pop_front":
        if end-begin-1==0:
            result.append(-1)
        else:
            result.append(deque[begin+1])
            deque[begin+1]=0
            begin+=1
    elif command[0]=="pop_back":
        if end-begin-1==0:
            result.append(-1)
        else:
            result.append(deque[end-1])
            deque[end-1]=0
            end-=1
    elif command[0]=="size":
        result.append(end-begin-1)
    elif command[0]=="empty":
        if end-begin-1==0:
            result.append(1)
        else:
            result.append(0)
    elif command[0]=="front":
        if end-begin-1==0:
            result.append(-1)
        else:
            result.append(deque[begin+1])
    elif command[0]=="back":
        if end-begin-1==0:
            result.append(-1)
        else:
            result.append(deque[end-1])

for r in result:
    print(r)
