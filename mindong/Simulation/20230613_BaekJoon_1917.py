corrs=[[] for _ in range(3)]
for corr in corrs:
    for _ in range(6):
        corr.append(list(map(int, input().split())))

reverse=[5,3,4,1,2,0]

def dfs(x, y, side, surround, corr):
    global sides, is_cube
    if not is_cube:
        return
    # print(x,y,side)
    if sides[side]:
        is_cube=False
        return
    corr[x][y]=0
    sides[side]=True
    for a, b in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if a<6 and b<6 and corr[a][b]==1:
            if [a, b]==[x+1, y]:
                dfs(a,b,surround[0], [reverse[side], surround[1], side, surround[3]], corr)
            if [a, b]==[x, y+1]:
                dfs(a,b,surround[1], [surround[0], reverse[side], surround[2], side], corr)
            if [a, b]==[x-1, y]:
                dfs(a,b,surround[2], [side, surround[1], reverse[side], surround[3]],corr)
            if [a, b]==[x, y-1]:
                dfs(a,b,surround[3], [surround[0], side, surround[2], reverse[side]], corr)

for corr in corrs:
    is_cube=True
    sides=[False for i in range(6)]
    for i in range(6):
        for j in range(6):
            if corr[i][j]==1:
                dfs(i,j,0, [1,2,3,4], corr)
                    
    if is_cube:
        print("yes")
    else:
        print("no")