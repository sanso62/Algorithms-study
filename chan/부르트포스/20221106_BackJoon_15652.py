# 15652번 N과 M(4)
def bruteforce(arr, st):
    global n,m
    if(len(arr) == m):
        for num in arr:
            print(str(num)+" ", end="")
        print()
        return

    for i in range(st,n+1):
        arr.append(i)
        bruteforce(arr, i)
        arr.pop()

n,m = map(int, input().split())
bruteforce([], 1)