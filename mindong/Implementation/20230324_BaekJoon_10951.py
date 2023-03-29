import sys
inputs=sys.stdin.read().splitlines()
result=[]
for input in inputs:
    a,b=map(int, input.split())
    result.append(a+b)

for r in result:
    print(r)
    