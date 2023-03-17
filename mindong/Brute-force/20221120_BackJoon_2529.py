k=int(input())
A=input().split()

nums1=[num for num in range(9,-1,-1)]
max_n=""
def find_max_n(a, l, li):
    global nums1
    global max_n
    for n in li:
        if n!=-1:
            max_n+=str(n)
            nums1[-n-1]=-1
            if len(max_n)==k+1:
                break
            elif a[l]=="<":
                find_max_n(a, l+1, nums1[:-n-1])
            elif a[l]==">":
                find_max_n(a, l+1, nums1[-n:])
            nums1[-n-1]=n
            if len(max_n)==k+1:
                break
            else:
                max_n=max_n[:-1]
                
find_max_n(A, 0, nums1)
print(max_n)

nums2=[num for num in range(10)]
min_n=""
def find_min_n(a, l, li):
    global nums2
    global min_n
    for n in li:
        if n!=-1:
            min_n+=str(n)
            nums2[n]=-1
            if len(min_n)==k+1:
                break
            elif a[l]=="<":
                find_min_n(a, l+1, nums2[n+1:])
            elif a[l]==">":
                find_min_n(a, l+1, nums2[:n])
            nums2[n]=n
            if len(min_n)==k+1:
                break
            else:
                min_n=min_n[:-1]
                
find_min_n(A, 0, nums2)
print(min_n)