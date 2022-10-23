# 2609번 - 최대공약수와 최소공배수

def gcd(a, b):
    while (b!=0):
        r = a%b
        a = b
        b = r

    return a

a,b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a*b//g)