# 15650번 N과 M(2)

def bruteforce(arr, st):
    global n,m
    if(len(arr) == m):
        for num in arr:
            print(str(num)+" ", end="")
        print()
        return

    for i in range(st,n+1):
        if(i not in arr):
            arr.append(i)
            bruteforce(arr, i+1)
            arr.pop()

n,m = map(int, input().split())
bruteforce([], 1)
