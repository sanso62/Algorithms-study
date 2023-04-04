import sys

inputs=sys.stdin.read().splitlines()
n,m,x,y,K=map(int,inputs[0].split())
Map=[]
for s in inputs[1:-1]:
    Map.append(list(map(int,s.split())))
k=list(map(int,inputs[-1].split()))
top,down,left,right,front,back=0,0,0,0,0,0
for op in k:
    # print(x,y,top,down,left,right,front,back)
    if op==1:
        if y+1>=m:
            continue
        y+=1
        top,down,left,right=right,left,top,down
        if Map[x][y]==0:
            Map[x][y]=down
        else:
            down=Map[x][y]
            Map[x][y]=0
        print(top)
    elif op==2:
        if  y-1<0:
            continue
        y-=1
        top,down,left,right=left,right,down,top
        if Map[x][y]==0:
            Map[x][y]=down
        else:
            down=Map[x][y]
            Map[x][y]=0
        print(top)
    elif op==3:
        if  x-1<0:
            continue
        x-=1
        top,down,front,back=back,front,top,down
        if Map[x][y]==0:
            Map[x][y]=down
        else:
            down=Map[x][y]
            Map[x][y]=0
        print(top)
    elif op==4:
        if  x+1>=n:
            continue
        x+=1
        top,down,front,back=front,back,down,top
        if Map[x][y]==0:
            Map[x][y]=down
        else:
            down=Map[x][y]
            Map[x][y]=0
        print(top)

