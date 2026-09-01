class Solution:
    def mergetwolist(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next

            curr = curr.next

        if curr1:
            curr.next = curr1

        if curr2:
            curr.next = curr2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(self.mergetwolist(list1, list2))

            lists = merged_lists

        return lists[0]