class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Get the cars in terms of position and speed, then sort by position in decreasing
        # Get the time to reach the target and if its equal to the prev_time, it is within the same fleet
        cars = []
        fleets = 0
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x:x[0], reverse=True)
        prev_time = None

        for pos, rate in cars:
            time = math.ceil(target - pos) / rate
            if not prev_time or time > prev_time:
                fleets += 1
                prev_time = time

        return fleets