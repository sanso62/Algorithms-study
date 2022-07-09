n, m=map(int, input().split())
li=[]
for _ in range(n):
    s=input()
    li.append(s)

for s in li:
    print(s[::-1])