# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next:
            next, cur.next=cur.next, cur.next.next
            next.next=cur
            cur=cur.next
            
            

        return head
        