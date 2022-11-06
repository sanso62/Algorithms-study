# 15651번 N과 M(3)

def bruteforce(arr):
    global n,m
    if(len(arr) == m):
        for num in arr:
            print(str(num)+" ", end="")
        print()
        return

    for i in range(1,n+1):
        arr.append(i)
        bruteforce(arr)
        arr.pop()

n,m = map(int, input().split())
bruteforce([])
