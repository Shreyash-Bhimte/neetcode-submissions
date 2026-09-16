# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr.next = head 

        slow,fast = dummy,dummy
        i = 0 
        while i < n:
            fast = fast.next
            i += 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return dummy.next