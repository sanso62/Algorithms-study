import sys

num=int(input())
inputs=sys.stdin.read().splitlines()
S=[]
for s in inputs:
    S.append(list(map(int, s.split())))

min=2001
def twoway(n, li, diff):
    global min
    if n==-1:
        if abs(diff) < min:
            min=abs(diff)
    else:
        twoway(n-1, li+[0], diff-sum([S[i][-n-1]+S[-n-1][i] for i in range(len(li)) if li[i]==0]))
        twoway(n-1, li+[1], diff+sum([S[i][-n-1]+S[-n-1][i] for i in range(len(li)) if li[i]==1]))
twoway(num-1, [], 0)
print(min)