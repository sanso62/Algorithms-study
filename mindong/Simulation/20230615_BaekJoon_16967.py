H, W, X, Y=map(int, input().split())

B=[]
for _ in range(H+X):
    B.append(list(map(int, input().split())))

A=[[-1]*W for _ in range(H)]
done=False
for i in range(len(B)):
    for j in range(len(B[0])):
        if i>=H or j>=W:
            continue
        if i+X<H and j+Y<W:
            if A[i][j]==-1:
                A[i][j]=B[i][j]
            A[i+X][j+Y]=B[i+X][j+Y]-A[i][j]
        else:
            if A[i][j]==-1:
                A[i][j]=B[i][j] 
            
    if done:
        break

for row in A:
    print(" ".join(map(str, row)))