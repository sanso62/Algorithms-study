# 148. Sort List
# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        node = head
        while node != None:
            li.append(node.val)
            node=node.next
        
        li.sort()
        
#       Quicksort 로 풀려고 했는데 안됨.
#       lo=0
#       hi=len(li)-1

#       def quicksort(li, lo, hi):
#             def partition(lo, hi):
#                 pivot=li[hi]
#                 left=lo
                
#                 for right in range(lo, hi):
#                     if li[right] < pivot:
#                         li[left], li[right] = li[right], li[left]
#                         left+=1
                
#                 li[left], li[hi] = li[hi], li[left]
#                 return left

#             if lo<hi:
#                 pivot=partition(lo, hi)
#                 quicksort(li, lo, pivot-1)
#                 quicksort(li, pivot+1, hi)
        
#         quicksort(li,lo,hi)
        
        
        prev: ListNode=None
        result: ListNode=None
        for i in li[::-1]:
            result=ListNode(i)
            result.next=prev
            prev=result
        
        return result

