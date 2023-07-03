sudoku1, sudoku2, sudoku3=[], [[] for _ in range(9)], [[] for _ in range(9)]
for i in range(9):
    row = list(map(int, input().split()))
    sudoku1.append(row)
for i, row in enumerate(sudoku1):
    [sudoku2[k].append(v) for k, v in enumerate(row)]
    sudoku3[(i//3)*3+0].extend(row[0:3])
    sudoku3[(i//3)*3+1].extend(row[3:6])
    sudoku3[(i//3)*3+2].extend(row[6:9])

found = False
def go(i, j, k, n):
    sudoku1[i][j], sudoku2[j][i], sudoku3[k][(i%3)*3+(j%3)] = n, n, n
    if j+1==9:
        dfs(i+1, 0)
    else:
        dfs(i, j+1)
    if found: return
    sudoku1[i][j], sudoku2[j][i], sudoku3[k][(i%3)*3+(j%3)] = 0, 0, 0

def dfs(i, j):
    global sudoku1, sudoku2, sudoku3, found 
    if i==9:
        found = True
        return
    if sudoku1[i][j]==0:
        for n in range(1, 10):
            if n not in sudoku1[i] and n not in sudoku2[j]:
                if 0<=i<3 and 0<=j<3 and n not in sudoku3[0]:
                    go(i, j, 0, n)
                if 0<=i<3 and 3<=j<6 and n not in sudoku3[1]:
                    go(i, j, 1, n)
                if 0<=i<3 and 6<=j<9 and n not in sudoku3[2]:
                    go(i, j, 2, n)
                if 3<=i<6 and 0<=j<3 and n not in sudoku3[3]:
                    go(i, j, 3, n)
                if 3<=i<6 and 3<=j<6 and n not in sudoku3[4]:
                    go(i, j, 4, n)
                if 3<=i<6 and 6<=j<9 and n not in sudoku3[5]:
                    go(i, j, 5, n)
                if 6<=i<9 and 0<=j<3 and n not in sudoku3[6]:
                    go(i, j, 6, n)
                if 6<=i<9 and 3<=j<6 and n not in sudoku3[7]:
                    go(i, j, 7, n)
                if 6<=i<9 and 6<=j<9 and n not in sudoku3[8]:
                    go(i, j, 8, n)
    else:
        if j+1==9:
            dfs(i+1, 0)
        else:
            dfs(i, j+1)
        

dfs(0, 0)

for li in sudoku1:
    print(" ".join(list(map(str, li))))