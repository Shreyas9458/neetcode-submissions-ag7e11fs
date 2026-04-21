# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = dummyHead = ListNode(0, None)

        while list1 and list2:
            if list1.val <= list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return head.next
        