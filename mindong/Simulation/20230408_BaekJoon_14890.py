import sys
inputs=sys.stdin.read().splitlines()
n,l=map(int, inputs[0].split())
rows=[]
columns=[[] for _ in range(n)]
for s in inputs[1:]:
    li=list(map(int, s.split()))
    rows.append(li)
    for i in range(n):
        columns[i].append(li[i])

way=0
for line in rows+columns:
    up, down, is_possible=[line[0]],[0,0],True
    used_i=101
    for i in range(1,n):
        # print(line[i],up, down, is_possible)
        if line[i]>line[i-1]:
            if line[i]-line[i-1]>1 or down!=[0,0]:
                is_possible=False
                break
            if len(up)<l:
                is_possible=False
                break
            else:
                if line[i]-up[-l]!=1 or used_i==i-l:
                    is_possible=False
                    break
                else:
                    up=[line[i]]
        elif line[i]<line[i-1]:
            if line[i-1]-line[i]>1 or down!=[0,0]:
                is_possible=False
                break
            if l!=1:
                down=[line[i-1],2]
            else:
                up=[]
                used_i=i
            up.append(line[i])
        elif line[i]==line[i-1]:
            up.append(line[i])
            if down[1]==l:
                if down[0]-line[i-1]==1:
                    down=[0,0]
                    up=[line[i]]
                    used_i=i
                else:
                    is_possible=False
                    break
            else:
                if down!=[0,0]:
                    down[1]+=1
    if down!=[0,0]:
        is_possible=False

    if is_possible:
        way+=1
        # print(line)

print(way)