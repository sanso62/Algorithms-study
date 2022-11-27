import sys

inputs=sys.stdin.read().splitlines()

def loop(l, numbers, n):
    for i in range(len(l)-n+1):
        if n==1:
            print(numbers+l[i])
        else:
            loop(l[i+1:], numbers+l[i]+" ", n-1)
           
for input in inputs:
    if input=="0":
        break
    li=input.split()[1:]
    loop(li, "", 6)
    print()