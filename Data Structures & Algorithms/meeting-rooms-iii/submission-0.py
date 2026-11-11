from heapq import heappush_max, heappop_max
class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Hashmap of each meeting room to a maxheap where we maxheap[0] is the earliest time that we can add another meeting (start >= maxheap[0])
        # If added, we check len(maxheap), if its greater than the current_max, we replace the current_max
        meetings.sort(key=lambda x: x[0])
        current_max = 0
        hashMap = defaultdict(list) # Maps each meeting room to a maxheap
        for start, end in meetings:
            found = False
            earliest_time, room = None, None
            for i in range(n):
                # Finds the first empty meeting room
                if not hashMap[i] or start >= hashMap[i][0]:
                    found = True
                    heappush_max(hashMap[i], end)
                    if len(hashMap[i]) > current_max:
                        current_max = len(hashMap[i])
                    break
                
                if not earliest_time:
                    earliest_time = hashMap[i][0]
                    room = i
                
                if earliest_time and hashMap[i][0] < earliest_time:
                    earliest_time = hashMap[i][0]
                    room = i
                
            # We could not find an empty meeting room, so we delay
            if not found:
                start, end = earliest_time, earliest_time + (end - start)
                heappush_max(hashMap[room], end)
                if len(hashMap[room]) > current_max:
                    current_max = len(hashMap[room])
                    
        for key, value in hashMap.items():
            if len(value) == current_max:
                return key
        
        return -1
