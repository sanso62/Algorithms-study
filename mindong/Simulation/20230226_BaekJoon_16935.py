import sys

n, m, n_k=map(int, input().split())
A=[]
for _ in range(n):
    r=list(map(int, input().split()))
    A.append(r)
K=list(map(int, input().split()))

for k in K:
    if k==1:
        K1(A)
    elif k==2:
        K2(A)
    elif k==3:
        K3(A)
    elif k==4:
        K4(A)
    elif k==5:
        K5(A)
    elif k==6:
        K6(A)
        








