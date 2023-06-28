N, M=map(int, input().split())
corr=[]
corr.append(["" for _ in range(M+2)])
for _ in range(N):
    corr.append([""]+list(input())+[""])
corr.append(["" for _ in range(M+2)])

c1, c2 = False, False
for i in range(1, N+1):
    for j in range(1, M+1):
        if corr[i][j]=="o":
            if not c1:
                c1=(i, j)
            else:
                c2=(i, j)

min_count=11
def go(x1, y1, x2, y2, count):
    global min_count
    # print(x1, y1)
    # print(x2, y2)
    if count>10 or (not corr[x1][y1] and not corr[x2][y2]):
        return
    if not corr[x1][y1] and corr[x2][y2]:
        if min_count>count:
            min_count=count
        return
    if corr[x1][y1] and not corr[x2][y2]:
        if min_count>count:
            min_count=count
        return
    for k, l in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        v1, v2=corr[x1+k][y1+l], corr[x2+k][y2+l]
        if (v1=="#" and v2=="#") or (v1=="#" and v2=="o") or (v1=="o" and v2=="#"):
            continue
        if v1=="#":
            go(x1, y1, x2+k, y2+l, count+1)
        elif v2=="#":
            go(x1+k, y1+l, x2, y2, count+1)
        else:
            go(x1+k, y1+l, x2+k, y2+l, count+1)

go(c1[0], c1[1], c2[0], c2[1], 0)
if min_count==11:
    print(-1)
else:
    print(min_count)