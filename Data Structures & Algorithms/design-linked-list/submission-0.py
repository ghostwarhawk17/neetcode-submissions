class LL:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        length = 0

        while curr:
            if length == index:
                return curr.val
            curr = curr.next
            length += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = LL(val, None, None)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = LL(val, None, None)

        if self.head is None:
            self.head = new_node
            return

        end = self.head

        while end.next:
            end = end.next

        end.next = new_node
        new_node.prev = end

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        length = 0
        curr = self.head
        newnode = LL(val, None, None)

        while curr:
            if length == index:
                prevnode = curr.prev

                newnode.prev = prevnode
                newnode.next = curr

                prevnode.next = newnode
                curr.prev = newnode

                return

            length += 1
            curr = curr.next

        # index == length means add at tail
        if length == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next

            if self.head:
                self.head.prev = None

            return

        length = 0
        curr = self.head

        while curr:
            if length == index:
                prevnode = curr.prev
                nextnode = curr.next

                prevnode.next = nextnode

                if nextnode:
                    nextnode.prev = prevnode

                return

            length += 1
            curr = curr.next