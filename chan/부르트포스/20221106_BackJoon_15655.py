# 15655번 N과 M(6)
def bruteforce(arr):
    global n,m,arr_value
    if(len(arr) == m):
        for num in arr:
            print(str(num)+" ", end="")
        print()
        return

    for i in arr_value:
        if(i not in arr):
            arr.append(i)
            bruteforce(arr)
            arr.pop()

n,m = map(int, input().split())
arr_value = map(int, input().split())
arr_value = list(arr_value)
arr_value.sort()
bruteforce([])