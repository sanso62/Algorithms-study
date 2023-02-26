n=int(input())
ans=[]
for _ in range(n):
    value=int(input())
    ans.append(value)

log=0
stack, li=[],[]
for num in ans:
    if log<num:
        while log<num:
            log+=1
            stack.append(log)
            li.append("+")
        stack.pop()
        li.append("-")
    elif log==num:
        stack.pop()
        li.append("-")
    elif log>num:
        if stack[-1]==num:
            stack.pop()
            li.append("-")
        else:    
            li=False
            break

if li:
    for i in li:
        print(i)
else:
    print("NO")
