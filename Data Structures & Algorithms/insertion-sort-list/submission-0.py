# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"),head)
        curr = head
        prev = dummy

        while curr:
            if prev.val <= curr.val:
                prev = curr
                curr = curr.next
                continue
            tmp = dummy
            while tmp.next.val < curr.val:
                tmp = tmp.next

            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr
            curr = prev.next

        return dummy.next
        