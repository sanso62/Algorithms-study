import sys

inputs=sys.stdin.read().splitlines()

s=set()
for input in inputs[1:]:
    l=input.split()
    if len(l)==2:
        op, x= l
        # print(op,x, s)
    elif len(l)==1:
        op=l[0]
        # print(op, s)
    if op=="add":
        s.add(x)
    elif op=="remove":
        if x in s:
            s.remove(x)
    elif op=="check":
        if x in s:
            print(1)
        else:
            print(0)
    elif op=="toggle":
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif op=="all":
        s={str(n) for n in range(1, 21)}
    elif op=="empty":
        s.clear()
            