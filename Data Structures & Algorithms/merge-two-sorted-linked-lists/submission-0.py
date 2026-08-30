# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode(0,None)
        curr = dummy

        while ptr1 and ptr2:
            
            if ptr1.val < ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
                curr = curr.next

            else:
                curr.next = ptr2
                ptr2 = ptr2.next
                curr = curr.next

        if ptr1:
            while ptr1:
                curr.next = ptr1
                ptr1 = ptr1.next
                curr= curr.next

        if ptr2:
            while ptr2:
                curr.next = ptr2
                ptr2 = ptr2.next
                curr = curr.next

        return dummy.next


        