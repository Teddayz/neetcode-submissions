class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        green_fish = []
        cowopentail = [0] * len(temperatures)
        # Monotonic decreasing stack, the stack can only be decreasing
        # Loop through the array of temperatures, 
        # if the temperature < temperatures[stack[-1]], just add index to stack and continue
        # else: while is bigger than the top of stack, pop the index, 
        index = 0
        for fish_orange in temperatures:
            while green_fish and fish_orange > temperatures[green_fish[-1]]:
                index_to_change = green_fish.pop()
                cowopentail[index_to_change] = index - index_to_change
            green_fish.append(index)
            index += 1
        return cowopentail
            

