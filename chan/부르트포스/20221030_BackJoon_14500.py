# 14500번 - 테트로미노

row, col = map(int, input().split())

arr = []
for _ in range(0,row):
    tmp = map(int, input().split())
    arr.append(list(tmp))
