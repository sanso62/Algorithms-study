# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        cur=result
        add=0
        while l1 or l2 or add==1:
            node=ListNode(add,None)
            if l1:
                node.val+=l1.val
                l1=l1.next
            if l2:
                node.val+=l2.val
                l2=l2.next
            
            if node.val>=10:
                node.val-=10
                add=1
            else:
                add=0
            
            cur.next=node
            cur=cur.next
        
        return result.next