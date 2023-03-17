n, m=list(map(int, input().split()))
X, Y=[],[]
for i in range(m):
    x,y=list(map(int, input().split()))
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
if n%2==0:
    x_middle=(X[m//2-1]+X[m//2])//2
    y_middle=(Y[m//2-1]+Y[m//2])//2
else:
    x_middle=X[(m+1)//2-1]
    y_middle=Y[(m+1)//2-1]

print(sum([abs(i-x_middle) for i in X])+sum([abs(i-y_middle) for i in Y]))