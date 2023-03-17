import sys

input=sys.stdin.read().splitlines()
n_list=list(map(int, input[:-1]))

def is_pn(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for n in n_list:
    for i in range(3,n//2+1, 2):
        if is_pn(i) and is_pn(n-i):
            print(f"{n} = {i} + {n-i}")
            break
