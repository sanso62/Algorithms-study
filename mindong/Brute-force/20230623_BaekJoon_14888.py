N=int(input())
A=list(map(int, input().split()))
operations=list(map(int,input().split()))

max_value=-1000000001
min_value=1000000001
def find(value, pos, ops):
    global max_value, min_value
    # print(value, pos, ops)
    if pos>=N:
        if max_value<value:
            max_value=value
        if min_value>value:
            min_value=value
        return
    for i in range(4):
        if ops[i]==0:
            continue
        ops[i]-=1
        if i==0:
            find(value+A[pos], pos+1, ops)
        elif i==1:
            find(value-A[pos], pos+1, ops)
        elif i==2:
            find(value*A[pos], pos+1, ops)
        elif i==3:
            if value<0 and A[pos]>0:
                find((value*(-1)//A[pos])*(-1), pos+1, ops)
            else:
                find(value//A[pos], pos+1, ops)
        ops[i]+=1
            
find(A[0], 1, operations)
print(max_value)
print(min_value)