import sys

inputs=sys.stdin.read().splitlines()
n, m, R=map(int, inputs[0].split())
cnt=[]
for s in inputs[1:-1]:
    cnt.append(list(map(int, s.split())))
ops=list(map(int, inputs[-1].split()))

def op1(r,c,arr):
    result=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            result[r-i-1][j]=arr[i][j]
    return [r,c,result]

def op2(r,c,arr):
    result=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            result[i][c-j-1]=arr[i][j]
    return [r,c,result]

def op3(r,c,arr):
    result=[[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][r-i-1]=arr[i][j]
    return [c,r,result]

def op4(r,c,arr):
    result=[[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[c-j-1][i]=arr[i][j]
    return [c,r, result]

def op5(r,c,arr):
    result=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i<r//2 and j<c//2:
                result[i][j+c//2]=arr[i][j]
            if i<r//2 and j>=c//2:
                result[i+r//2][j]=arr[i][j]
            if i>=r//2 and j>=c//2:
                result[i][j-c//2]=arr[i][j]
            if i>=r//2 and j<c//2:
                result[i-r//2][j]=arr[i][j]
    return [r,c,result]

def op6(r,c,arr):
    result=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i<r//2 and j<c//2:
                result[i+r//2][j]=arr[i][j]
            if i<r//2 and j>=c//2:
                result[i][j-c//2]=arr[i][j]
            if i>=r//2 and j>=c//2:
                result[i-r//2][j]=arr[i][j]
            if i>=r//2 and j<c//2:
                result[i][j+c//2]=arr[i][j]
    return [r,c,result]

for op in ops:
    if op==1:
        n,m,cnt=op1(n,m,cnt)
    elif op==2:
        n,m,cnt=op2(n,m,cnt)
    elif op==3:
        n,m,cnt=op3(n,m,cnt)
    elif op==4:
        n,m,cnt=op4(n,m,cnt)
    elif op==5:
        n,m,cnt=op5(n,m,cnt)
    elif op==6:
        n,m,cnt=op6(n,m,cnt)

for i in range(n):
    li_s=list(map(str, cnt[i]))
    print(" ".join(li_s))
