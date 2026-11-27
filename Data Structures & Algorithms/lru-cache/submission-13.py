from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderedDict = OrderedDict() # Last is most recently used

    def get(self, key: int) -> int:
        if key in self.orderedDict:
            self.orderedDict.move_to_end(key)
            return self.orderedDict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.orderedDict:
            self.orderedDict.move_to_end(key)
            self.orderedDict[key] = value
        else:
            self.orderedDict[key] = value
            if len(self.orderedDict) > self.capacity:
                self.orderedDict.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)