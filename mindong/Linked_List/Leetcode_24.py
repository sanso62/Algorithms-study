# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next:
            next, cur.next=cur.next, cur.next.next
            next.next=cur
            cur=cur.next
            
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        if not node or not node.next:
            return node
        cur, next=node, node.next
        cur.next=cur.next.next
        next.next=cur
        node=next
        node.next.next=self.swapPairs(node.next.next)
        return node
        
        
        