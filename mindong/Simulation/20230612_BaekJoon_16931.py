N, M = map(int, input().split())
corr=[]
for _ in range(N):
    corr.append(list(map(int, input().split())))

total=0
for x in range(N):
    for y in range(M):
        if x-1<0 or corr[x][y] > corr[x-1][y]:
            if x-1<0: total+=corr[x][y]
            else: total+=corr[x][y]-corr[x-1][y]
        if y-1<0 or corr[x][y] > corr[x][y-1]:
            if y-1<0: total+=corr[x][y]
            else: total+=corr[x][y]-corr[x][y-1]
        if x+1>=N or corr[x][y] > corr[x+1][y]:
            if x+1>=N: total+=corr[x][y]
            else: total+=corr[x][y]-corr[x+1][y]
        if y+1>=M or corr[x][y] > corr[x][y+1]:
            if y+1>=M: total+=corr[x][y]
            else: total+=corr[x][y]-corr[x][y+1]

print(total+N*M*2)