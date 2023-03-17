# N, M, K=map(int, input().split())
# Coor=[]
# for _ in range(N):
#     row=list(map(int, input().split()))
#     Coor.append(row)

import sys

inputs = sys.stdin.read().splitlines()
N, M, K = map(int, inputs[0].split())
Coor = []
for r in inputs[1:]:
    row = list(map(int, r.split()))
    Coor.append(row)

def select_and_plus(sum, max, coor, n, m, k):
    if k==K-1:
        coor[n][m]=False
        if n+1<N:
            coor[n+1][m]=False
        if m+1<M:
            coor[n][m+1]=False
    for i in range(n,N):
        if i>n:
            m=0
        for j in range(m,M):
            if coor[i][j] is False:
                continue
            else:
                sum+=coor[i][j]
                coor[i][j]=False
                if i+1<N:
                    coor[i+1][j]=False
                if j+1<M:
                    coor[i][j+1]=False
                if k==1:
                    print("***",i,j)
                    for ro in coor:
                        print(ro)
                    if sum>max:
                        max=sum
                    return max
                else:
                    print("**",i,j)
                    for ro in coor:
                        print(ro)
                    k-=1
                    max = select_and_plus(sum, max, coor, i, j, k)
    return max
    
Max=-40000
for a in range(N):
    for b in range(M):
        print("*",a,b)
        Sum=select_and_plus(Coor[a][b], Max, Coor, a, b, K-1)
        if Sum>Max:
            Max=Sum
print(Max)