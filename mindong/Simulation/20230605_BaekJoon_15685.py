N=int(input())
li_dc=[]
for _ in range(N):
    li_dc.append(list(map(int, input().split())))

cor=[[False]*101 for _ in range(101)]
def draw(x, y, g, count, dir):
    global cor
    add_dir=[]
    print(dir)
    for i,d in enumerate(dir[::-1]):
        if d == 0:
            if i<len(dir)//2:
                x+=1
            add_dir.append(1)
        elif d==1:
            if i<len(dir)//2:
                y-=1
            add_dir.append(2)
        elif d==2:
            if i<len(dir)//2:
                x-=1
            add_dir.append(3)
        elif d==3:
            if i<len(dir)//2:
                y+=1
            add_dir.append(0)
        if 0<=x<=100 and 0<=y<=100:
            cor[y][x]=True
            print(x, y, cor[y][x], d)
    if count+1<=g:
        draw(x,y,g,count+1,dir+add_dir)
    else:
        return
            
        

for dc in li_dc:
    cor[dc[1]][dc[0]]=True
    if dc[2] ==0:
        cor[dc[1]][dc[0]+1]=True
    elif dc[2]==1:
        cor[dc[1]][dc[0]]=True
    elif dc[2]==2:
        cor[dc[1]][dc[0]]=True
        print(dc[0], dc[1], cor[dc[1]][dc[0]])
    draw(dc[0], dc[1], dc[3], 0, [dc[2]])

result=0
for i in range(101):
    for j in range(101):
        if cor[i][j]:
            if cor[i+1][j] and cor[i][j+1] and cor[i+1][j+1]:
                result+=1


print(result)