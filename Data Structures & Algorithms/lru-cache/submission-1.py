class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node((0, 0), None, None)
        self.tail = self.Node((0, 0), None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map.get(key)
            self.deleteNode(node)
            self.addToList(node)
            return node.keyValue[1]
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            old_node = self.hash_map.get(key)
            self.deleteNode(old_node)
            new_node = self.Node((key, value), None, None)
            self.hash_map[key] = new_node
            self.addToList(new_node)
        else:
            if len(self.hash_map) == self.capacity:
                node_to_remove = self.tail.prev
                print(node_to_remove.keyValue)
                del self.hash_map[node_to_remove.keyValue[0]]
                self.deleteNode(node_to_remove)
            node_to_add = self.Node((key, value), None, None)
            self.hash_map[key] = node_to_add
            self.addToList(node_to_add)

    
    def deleteNode(self, node: Node) -> None:
        next = node.next
        prev = node.prev
        prev.next = node.next
        next.prev = prev

    def addToList(self, node: Node) -> None:
        next = self.head.next
        node.next = next
        next.prev = node
        node.prev = self.head
        self.head.next = node

    class Node:
        
        def __init__(self, keyValue: tuple, prev: Node, next: Node):
            self.keyValue = keyValue
            self.prev = None
            self.next = None
