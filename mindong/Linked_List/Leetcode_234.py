# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev=head
        half=head
        n=0
        while half and half.next:
            n+=1
            head=head.next
            half=half.next.next
            if half and not half.next:
                head=head.next
        
        reverse=None
        while head:
            temp=ListNode(head.val, reverse)
            reverse=temp
            head=head.next
        
        while prev and reverse:
            if prev.val!=reverse.val:
                return False
            prev=prev.next
            reverse=reverse.next
            
        return True