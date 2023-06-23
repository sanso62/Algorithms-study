N, M=map(int, input().split())
corr=[]
for _ in range(N):
    corr.append(list(map(int, input().split())))
check=[[False]*M for _ in range(N)]
max_value=0
def tetromino(x, y, value, count):
    global max_value, check
    if count==4:
        if max_value<value:
            max_value=value
        return
    for nx, ny in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
        if 0<=nx<N and 0<=ny<M:
            if not check[nx][ny]:
                check[nx][ny]=True
                tetromino(nx, ny, value+corr[nx][ny], count+1)
                check[nx][ny]=False
    
for i in range(N):
    for j in range(M):
        check[i][j]=True
        tetromino(i, j, corr[i][j], 1)
        check[i][j]=False
        for case in [((i, j-1), (i, j+1), (i+1, j)), ((i, j-1), (i, j+1), (i-1, j)), ((i-1, j), (i, j+1), (i+1, j)), ((i-1, j), (i, j-1), (i+1, j))]:
            is_possible=True
            value=corr[i][j]
            for n, m in case:
                if 0<=n<N and 0<=m<M:
                    value+=corr[n][m]
                else:
                    is_possible=False
                    break
            if is_possible:
                tetromino(i, j, value, 4)                  

print(max_value)