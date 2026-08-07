class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        biggest_element_prefix = 0
        biggest_element_suffix = 0
        j = len(height) - 1
        for i in range(len(height)):
            if height[i] > biggest_element_prefix:
                biggest_element_prefix = height[i]
            if height[j - i] > biggest_element_suffix:
                biggest_element_suffix = height[j - i]
            prefix.append(biggest_element_prefix)
            suffix.append(biggest_element_suffix)    
        suffix.reverse()
        max_water = 0
        for i in range(len(height)):
            max_water += min(prefix[i], suffix[i]) - height[i]
        return max_water

