class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            self.insertToHead(node)
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            node.value = value
            self.insertToHead(node)
        else:
            if len(self.hashMap) == self.capacity:
                # evict
                nodeToRemove = self.tail.prev
                del self.hashMap[nodeToRemove.key]
                self.remove(nodeToRemove)
            node = Node(key, value)
            self.hashMap[key] = node
            self.insertToHead(node)
                
    
    def insertToHead(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)