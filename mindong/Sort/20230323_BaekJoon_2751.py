import sys
inputs=sys.stdin.read().splitlines()
li=list(map(int, inputs[1:]))

li.sort()
for v in li:
    print(v)