class LL:
    def __init__(self, prev=None, next=None, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = prev
        self.next = next


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        # key -> node
        self.cache = {}

        # frequency -> doubly linked list
        self.freq_list = {}

    def add_node(self, node):
        freq = node.freq

        if freq not in self.freq_list:
            self.freq_list[freq] = [None, None]

        head, tail = self.freq_list[freq]

        # insert at front
        if head is None:
            self.freq_list[freq][0] = node
            self.freq_list[freq][1] = node
        else:
            node.next = head
            head.prev = node
            self.freq_list[freq][0] = node

    def remove_node(self, node):
        freq = node.freq

        head, tail = self.freq_list[freq]

        if node.prev:
            node.prev.next = node.next
        else:
            self.freq_list[freq][0] = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.freq_list[freq][1] = node.prev

        node.prev = None
        node.next = None

    def increase_freq(self, node):
        old_freq = node.freq

        self.remove_node(node)

        # If this was the last node with minimum frequency
        if old_freq == self.min_freq:
            if self.freq_list[old_freq][0] is None:
                self.min_freq += 1

        node.freq += 1

        self.add_node(node)

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Accessing the node increases frequency
        self.increase_freq(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.increase_freq(node)
            return

        # Cache is full
        if self.size == self.capacity:

            # Remove least recently used node
            # from the minimum frequency list
            head, tail = self.freq_list[self.min_freq]

            remove_node = tail

            self.remove_node(remove_node)

            del self.cache[remove_node.key]

            self.size -= 1

        # Add new node
        new_node = LL(key=key, val=value)

        self.cache[key] = new_node

        self.add_node(new_node)

        self.min_freq = 1
        self.size += 1