N, R = map(int, input().split())
N=2**N
A=[]
ops=[]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(R):
    ops.append(list(map(int, input().split())))

def op1(x,y,nn):
    global result, A
    for a in range(x, x+2**nn):
        for b in range(y, y+2**nn):
            result[x+x+2**nn-a-1][b], A[a][b]=A[a][b], result[x+x+2**nn-a-1][b]

def op2(x,y,nn):
    global result, A
    for a in range(x, x+2**nn):
        for b in range(y, y+2**nn):
            result[a][y+y+2**nn-b-1], A[a][b]=A[a][b], result[x+x+2**nn-a-1][b]

def op3(x, y, nn):
    global result, A
    for a in range(2**nn):
        for b in range(2**nn):
            result[x+b][y+2**nn-a-1], A[x+a][y+b]=A[x+a][y+b], result[x+b][y+2**nn-a-1]

def op4(x, y, nn):
    global result, A
    for a in range(2**nn):
        for b in range(2**nn):
            result[x+2**nn-b-1][y+a], A[x+a][y+b]=A[x+a][y+b], result[x+2**nn-b-1][y+a]
def op5678(x, y, nn, nx, ny):
    global result, A
    for a in range(2**nn):
        for b in range(2**nn):
            result[nx+a][ny+b], A[x+a][y+b]=A[x+a][y+b],result[nx+a][ny+b]

result=[([c for c in r]) for r in A]
for op, n in ops:
    if op==1 and n!=0:
        for i in range(0, N, 2**n):
            for j in range(0, N, 2**n):
                op1(i,j,n)
    elif op==2 and n!=0:
        for i in range(0, N, 2**n):
            for j in range(0, N, 2**n):
                op2(i,j,n)
    elif op==3 and n!=0:
        for i in range(0, N, 2**n):
            for j in range(0, N, 2**n):
                op3(i,j,n)
    elif op==4 and n!=-0:
        for i in range(0, N, 2**n):
            for j in range(0, N, 2**n):
                op4(i,j,n)
    elif op==5:
        sqr_n=2**n
        for i in range(0, N//sqr_n):
            for j in range(0, N//sqr_n):
                op5678(sqr_n*i,sqr_n*j,n,sqr_n*(N//sqr_n-i-1), sqr_n*j)
    elif op==6:
        sqr_n=2**n
        for i in range(0, N//sqr_n):
            for j in range(0, N//sqr_n):
                op5678(sqr_n*i,sqr_n*j,n,sqr_n*i, sqr_n*(N//sqr_n-j-1))
    elif op==7:
        sqr_n=2**n
        for i in range(0, N//sqr_n):
            for j in range(0, N//sqr_n):
                op5678(sqr_n*i,sqr_n*j,n,sqr_n*j, sqr_n*(N//sqr_n-i-1))
    elif op==8:
        sqr_n=2**n
        for i in range(0, N//sqr_n):
            for j in range(0, N//sqr_n):
                op5678(sqr_n*i,sqr_n*j,n,sqr_n*(N//sqr_n-j-1),sqr_n*i)
    A=[([c for c in r]) for r in result]

for r in result:
    print(" ".join(list(map(str, r))))