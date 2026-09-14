class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key : node
        self.capacity = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.left.next = self.right
        self.right.prev = self.left # left ->right
                                    # left <-right


    def remove(self,node):
        prevA = node.prev
        nxtB = node.next

        prevA.next = nxtB
        nxtB.prev = prevA

    def insert(self,node):
        real = self.right.prev
        rightNode = self.right
        real.next = node
        rightNode.prev = node
        node.next = rightNode
        node.prev = real



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])


        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
