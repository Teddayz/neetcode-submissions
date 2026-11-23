from collections import defaultdict
class TimeMap:

    def __init__(self):
        # Contains a hashmap to a list of (timestamp, value)
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.hash_map.get(key, [])
        left, right = 0, len(lst) - 1
        if not lst or timestamp < lst[left][0]:
            return ""
        # Finds the biggest timestamp <= timestamp
        while left <= right:
            mid = (left + right) // 2
            if timestamp == lst[mid][0]:
                return lst[mid][1]
            elif timestamp < lst[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return lst[right][1]
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)