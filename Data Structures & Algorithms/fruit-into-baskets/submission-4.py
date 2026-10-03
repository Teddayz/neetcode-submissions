class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        hashMap = {}
        max_fruits = 0
        # Sliding window question. If the number of unique fruits <= 2, 
        # i can expand my right pointer
        # If there are more than 2 unique fruits, 
        # i must shift left pointer until theres only two unique fruits
        while right < len(fruits):
            if fruits[right] not in hashMap:
                hashMap[fruits[right]] = 0
            hashMap[fruits[right]] += 1
            while left < right and len(hashMap) > 2:
                curr_fruit = fruits[left]
                hashMap[curr_fruit] -= 1
                if hashMap[curr_fruit] == 0:
                    del hashMap[curr_fruit]
                left += 1
            max_fruits = max(right - left + 1, max_fruits)
            right += 1
                    
        return max_fruits
        
