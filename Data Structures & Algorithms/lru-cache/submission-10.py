from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderedDict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.orderedDict:
            return -1
        self.orderedDict.move_to_end(key, last=True)
        return self.orderedDict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.orderedDict:
            self.orderedDict[key] = value
            self.orderedDict.move_to_end(key, last=True)
        elif len(self.orderedDict) == self.capacity:
            self.orderedDict.popitem(last=False)
        self.orderedDict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)