import sys
sys.setrecursionlimit(10**6)
def main():
    global cnt
    global done
    inputs=sys.stdin.read().splitlines()
    n,m=map(int, inputs[0].split())
    r,c,d=map(int, inputs[1].split())
    cnt=[[1]*(m+2)]
    for s in inputs[2:]:
        cnt.append([1]+list(map(int, s.split()))+[1])
    cnt+=[[1]*(m+2)]
    # print(cnt)
    done=False
    cleaning(r+1,c+1,d,1)

def cleaning(x,y,dir,count):
    global cnt
    global done
    if done:
        return
    # print(x,y)
    cnt[x][y]=2
    destinations=found(x,y,cnt)
    if not destinations:
        if dir in [0,2]:
            if cnt[x+1-dir][y]==1:
                print(count)
                done==True
                return
            else:
                cleaning(x+1-dir, y, dir, count)
        elif dir in [1,3]:
            if cnt[x][y+dir-2]==1:
                done==True
                print(count)
                return
            else:
                cleaning(x, y+dir-2, dir, count)
    else:
        count+=1
        while True:
            dir=dir-1 if dir-1>=0 else 3
            if dir in destinations:
                break
        if dir==0:
            cleaning(x-1, y, dir, count)
        elif dir==1:
            cleaning(x, y+1, dir, count)
        elif dir==2:
            cleaning(x+1, y, dir, count)
        elif dir==3:
            cleaning(x, y-1, dir, count)

def found(a,b,cnt):
    dest=[]
    if cnt[a-1][b]==0:
        dest.append(0)
    if cnt[a][b+1]==0:
        dest.append(1)
    if cnt[a+1][b]==0:
        dest.append(2)
    if cnt[a][b-1]==0:
        dest.append(3)
    return dest

if __name__=="__main__":
    main()

