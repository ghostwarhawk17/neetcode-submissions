class LL: 
    def __init__(self, key=None, val=None, prev=None, next=None): 
        self.key = key 
        self.val = val 
        self.prev = prev 
        self.next = next 


class LRUCache: 
 
    def __init__(self, capacity: int): 
        self.capacity = capacity 
        self.cache = {} 

        self.left = LL(0, 0) 
        self.right = LL(0, 0) 

        self.left.next = self.right 
        self.right.prev = self.left 
 
    def insert(self, node): 
        prevnode, nextnode = self.right.prev, self.right

        prevnode.next = node 
        node.prev = prevnode         

        node.next = nextnode          
        nextnode.prev = node          
 
    def remove(self, node): 
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv
         
 
    def get(self, key: int) -> int: 
        if key in self.cache: 
            self.remove(self.cache[key]) 
            self.insert(self.cache[key]) 
            return self.cache[key].val 

        return -1 
         
    def put(self, key: int, value: int) -> None: 
        if key in self.cache: 
            self.remove(self.cache[key]) 

        self.cache[key] = LL(key, value) 
        self.insert(self.cache[key]) 
 
        if len(self.cache) > self.capacity: 
            lru = self.left.next 
            self.remove(lru) 
            del self.cache[lru.key]