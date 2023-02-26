n, k=map(int, input().split())
nodes=[]
type="m"

if k<=n:
    print(n-k)
else:
    t=1

def confirm_and_next(node, type):
    global t
    if type=="m":
        nodes.append(node-1)
        nodes.append(node+1)
    elif type=="l":
        nodes.append(node-1)
    elif type=="r":
        nodes.append(node+1)
    
    if node%2==0:
        nodes.append(node//2)
    
    if n in nodes:
        return 1
    
    

    
    