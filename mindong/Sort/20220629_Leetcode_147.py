# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        result=ListNode(head.val)
        head=head.next
        node=ListNode(head.val)
        
        if result.val>=node.val:
            node.next=result
            result=node
        else: 
            result.next=node
            
        del node
        
        head=head.next
        while head:
            right=result.next
            left=result
            node=ListNode(head.val)
            while right:    
                if left.val>=node.val:
                    node.next=left
                    result=node
                    break
                elif left.val<=node.val<=right.val:
                    node.next=right
                    left.next=node
                    break
                elif node.val>=right.val:
                    left=left.next
                    right=right.next
                    if not right:
                        left.next=node
            del node
            head=head.next
            
        return result
                