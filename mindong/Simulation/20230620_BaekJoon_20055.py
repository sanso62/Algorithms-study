N, K=map(int, input().split())
A=list(map(int, input().split()))
robot_exists=[False for _ in range(2*N)]
robots=[]
count, result=0,0

begin, end=0,0
while count<K:
    count=0
    result+=1
    if begin == 0: begin=2*N-1
    else: begin-=1
    if end == 0: end=2*N-1
    else: end-=1
    for i in range(len(robots)):
        if robots[i]==0: robots[i]=2*N-1
        else: robots[i]-=1

    if robots:
        for i, robot in enumerate(robots):
            if robot+1==2*N:
                next=0
            else:
                next=robot+1
            if not robot_exists[next] and A[next]>0:
                robot_exists[robot], robot_exists[next]=False, True
                A[next]-=1
                robots[i]=next

    if A[begin]>0 and not robot_exists[begin]:
        robots.append(begin)
        A[begin]-=1
        robot_exists[begin]=True
    print(len(robots))
    print(A)

    for v in A:
        if v<=0: count+=1

print(result)

                    
                    
                    


    
    