# Time: O(n) Extra space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # finding middle
        slow,fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse second half
        prev = None
        next_node = ListNode()
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # weave both 
        p1,p2 = head,prev
        while p2:
                p1_next,p2_next = p1.next,p2.next
                p1.next = p2
                if p1_next:
                    p2.next = p1_next
                p1,p2 = p1_next,p2_next




