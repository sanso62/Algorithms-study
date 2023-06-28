N=int(input())

result=0
def down(x, check_column, check_diagonal1, check_diagonal2):
    global result
    if x==N:
        result+=1
        return

    for y in range(N):
        if not check_column[y] and not check_diagonal1[x-y] and not check_diagonal2[x+y]:
            check_column[y], check_diagonal1[x-y], check_diagonal2[x+y]=True, True, True
            down(x+1, check_column, check_diagonal1, check_diagonal2)
            check_column[y], check_diagonal1[x-y], check_diagonal2[x+y]=False, False, False

init_check_column=[False for _ in range(N)]
init_check_diagonal1, init_check_diagonal2 = {}, {}
for i in range(N):
    for j in range(N):
        init_check_diagonal1[i-j]=False
        init_check_diagonal2[i+j]=False
down(0, init_check_column, init_check_diagonal1, init_check_diagonal2)
print(result)