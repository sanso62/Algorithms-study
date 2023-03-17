import sys

num=int(input())
inputs=sys.stdin.read().splitlines()
S=[]
for s in inputs:
    S.append(list(map(int, s.split())))

min=2001
def twoway(n, li,diff, k, l):
    global min
    if k==0 or l==0:
        if k==0:
            for j in range(-n-1,0):
                li+=[1]
                diff+=sum([S[i][j]+S[j][i] for i in range(len(li)) if li[i]==1])
        elif l==0:
            for j in range(-n-1,0):
                li+=[0]
                diff-=sum([S[i][j]+S[j][i] for i in range(len(li)) if li[i]==0])    
        # print(li)                   
        if abs(diff) < min:
            min=abs(diff)
    else:
        twoway(n-1, li+[0],diff-sum([S[i][-n-1]+S[-n-1][i] for i in range(len(li)) if li[i]==0]) ,k-1, l)
        twoway(n-1, li+[1],diff+sum([S[i][-n-1]+S[-n-1][i] for i in range(len(li)) if li[i]==1]) ,k, l-1)
twoway(num-1, [],0, num//2, num//2)
print(min)