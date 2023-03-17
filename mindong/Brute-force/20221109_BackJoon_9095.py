n_test_case=int(input())
test_case=[]
for _ in range(n_test_case):
    test_case.append(int(input()))
    
def move_add(li, idx):
    global num        
    # print(li, idx)
    for i in range(idx,len(li)-1):
        if li[i]+li[i+1]<4:
            num+=1
            if i+2<=len(li):
                move_add(li[:i]+[li[i]+li[i+1]]+li[i+2:], i)              
                
for n in test_case:
    num=1
    li=[1 for _ in range(n)]
    move_add(li, 0)
    print(num) 