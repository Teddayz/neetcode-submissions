class Node:

    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {} # Stores key to node

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.deleteNode(node)
        self.addToFront(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            newNode = Node(key, value, None, None)
            oldNode = self.hash_map[key]
            self.deleteNode(oldNode)
            self.addToFront(newNode)
            self.hash_map[key] = newNode
        else:
            newNode = Node(key, value, None, None)
            self.addToFront(newNode)
            self.hash_map[key] = newNode
            if len(self.hash_map) > self.capacity:
                # Evict
                oldNode = self.tail.prev
                self.hash_map.pop(oldNode.key)
                self.deleteNode(oldNode)


    def addToFront(self, node):
        nxt = self.head.next
        node.next = nxt
        nxt.prev = node
        self.head.next = node
        node.prev = self.head
    
    def deleteNode(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        
