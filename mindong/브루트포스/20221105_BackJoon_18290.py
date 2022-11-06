N, M, K=map(int, input().split())
Coor=[]
for _ in range(N):
    row=list(map(int, input().split()))
    Coor.append(row)

def select_and_plus(sum, coor, n, m, k):
    for i in range(n,N):
        if i>n:
            m=0
        for j in range(m,M):
            if coor[i][j] is not False:
                sum+=coor[i][j]
                coor[i][j]=False
                if i+1<N:
                    coor[i+1][j]=False
                elif j+1<M:
                    coor[i][j+1]=False
                break
    if k==1:
        return sum
    else:
        k-=1
        return select_and_plus(sum, coor, i, j, k)
    
max=-40000
for a in range(N):
    for b in range(M):
        Sum=select_and_plus(0, Coor, a, b, K)
        if Sum>max:
            max=Sum
print(max)