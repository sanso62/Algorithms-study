# import sys
n=int(input())
T, P=[], []
for _ in range(n):
    t,p=list(map(int, input().split()))
    T.append(t)
    P.append(p)

# inputs=sys.stdin.read().splitlines()
# for input in inputs:
#     t,p=list(map(int, input.split()))
#     T.append(t)
#     P.append(p)

max=0
def find_max_gain(idx, gain):
    global max
    for i in range(idx,n):
        if T[i]+i<=n:
            # print("*",idx, i, gain)
            gain+=P[i]
            find_max_gain(T[i]+i, gain)
            gain-=P[i]
            # print("***", idx,i, gain)    
        # else:
            # print("**",idx,i, gain)
    if gain>max:
        max=gain
    return

find_max_gain(0, 0)
print(max)


    