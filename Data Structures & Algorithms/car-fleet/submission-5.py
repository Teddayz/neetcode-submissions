class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hash_map = {}
        sorted_pos_to_speed = {}
        stack = []
        numOfFleets = 0
        for i in range(len(position)):
            hash_map[position[i]] = speed[i]
        for pos in sorted(hash_map.keys(), reverse=True):
            sorted_pos_to_speed[pos] = hash_map.get(pos)
        for pos in sorted_pos_to_speed.keys():
            time = (target - pos) / sorted_pos_to_speed.get(pos)
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)

        