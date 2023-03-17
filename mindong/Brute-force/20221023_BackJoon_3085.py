import sys

inputs=sys.stdin.read().splitlines()
n, board=int(inputs[0]), [list(s) for s in inputs[1:]]

max_l=0
location=[]
for i in range(n):
    start, end, l=0,0,0
    for j in range(n):
        if j==0:
            l+=1
            continue
        if board[i][j-1]==board[i][j]:
            l+=1
            end=j
            if j==n-1:
                if l>max_l:
                    max_l=l
                    location=[]
                    location.append((i, (start,end)))
                elif l==max_l:
                    location.append((i,(start,end)))
        else:
            if l>max_l:
                max_l=l
                location=[]
                location.append((i, (start,end)))
            elif l==max_l:
                location.append((i,(start,end)))
            start=j
            
for j in range(n):
    start, end, l=0,0,0
    for i in range(n):
        if i==0:
            l+=1
            continue
        if board[i-1][j]==board[i][j]:
            l+=1
            end=i
            if i==n-1:
                if l>max_l:
                    max_l=l
                    location=[]
                    location.append(((start,end),j))
                elif l==max_l:
                    location.append(((start,end),j))
        else:
            if l>max_l:
                max_l=l
                location=[]
                location.append(((start,end),j))
            elif l==max_l:
                location.append(((start,end),j))
            start=i

done=False
if max_l==n:
    print(max_l)
else:
    for k in location:
        if type(k[0]) is int:
            val=board[k[0]][k[1][0]]
            cor1=(k[0], k[1][0]-1)
            cor2=(k[0], k[1][1]+1)
            cors1=[(cor1[0]-1, cor1[1]), (cor1[0]+1, cor1[1]), (cor1[0], cor1[1]-1)]
            cors2=[(cor2[0]-1, cor2[1]), (cor2[0]+1, cor2[1]), (cor2[0], cor2[1]+1)]
        else:
            val=board[k[0][0]][k[1]]
            cor1=(k[0][0]-1, k[1])
            cor2=(k[0][1]+1, k[1])
            cors1=[(cor1[0]-1, cor1[1]), (cor1[0], cor1[1]+1), (cor1[0], cor1[1]-1)]
            cors2=[(cor2[0]+1, cor2[1]), (cor2[0], cor2[1]-1), (cor2[0], cor2[1]+1)]         
        
        for cor in cors1:
            if 0<=cor[0]<n and 0<=cor[1]<n:
                if board[cor[0]][cor[1]]==val:
                    max_l+=1
                    done=True
                    break
        if done:
            break
        for cor in cors2:
            if 0<=cor[0]<n and 0<=cor[1]<n:
                if board[cor[0]][cor[1]]==val:
                    max_l+=1
                    done=True
                    break
        if done:
            break   
    print(max_l)
            
                
                


    
    
                
        
        
    