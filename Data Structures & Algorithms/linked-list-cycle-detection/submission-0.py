# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next

        while fast:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    fast = fast.next
        return False