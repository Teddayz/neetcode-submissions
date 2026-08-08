class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        else:
            # List of tuples
            curr_list = self.hash_map.get(key)

            # Left is first timestamp
            left = 0
            right = len(curr_list) - 1

            if timestamp < curr_list[0][0]:
                return ""
            
            # Find the largest timestamp such that it is smaller than timestamp

            while left <= right:
                middle = (left + right) // 2
                middle_timestamp = curr_list[middle][0]
                if timestamp == middle_timestamp:
                    return curr_list[middle][1]

                elif timestamp < middle_timestamp:
                    right = middle - 1
                else:
                    left = middle + 1
                
            # print(left)
            # print(right)
            return curr_list[right][1]

            
        
