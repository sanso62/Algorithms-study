n=int(input())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int, input().split())))
triangle=triangle[::-1]

for i in range(n-1):
    # print(triangle[i])
    for j in range(n-i-1):
        triangle[i+1][j]+=max(triangle[i][j], triangle[i][j+1])

print(triangle[-1][0])