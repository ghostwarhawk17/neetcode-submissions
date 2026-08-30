# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next

        rev_ans = ans[::-1]
        return ans == rev_ans
        