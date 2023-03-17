import sys

inputs=sys.stdin.read().splitlines()
n, divisors =int(inputs[0]), list(map(int, inputs[1].split()))
divisors.sort()
if n==1:
    print(divisors[0]**2)
else:
    print(divisors[0]*divisors[-1])