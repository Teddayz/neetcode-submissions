import random
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        def partition(low: int, high: int) -> None:

            if low >= high:
                return 

            pivot = random.randint(low, high)
            nums[pivot], nums[high] = nums[high], nums[pivot]
            # Initialise the pointers
            left = low - 1
            middle = low - 1
            right = high
            target = nums[high]
            i = low
            while i < right:
                if nums[i] < target:
                    left += 1
                    nums[left], nums[i] = nums[i], nums[left]
                    middle += 1
                    i += 1
                elif nums[i] == target:
                    middle += 1
                    nums[i], nums[middle] = nums[middle], nums[i]
                    i += 1
                else:
                    right -= 1
                    nums[i], nums[right] = nums[right], nums[i]

            nums[right], nums[high] = nums[high], nums[right]
            partition(low, left)
            partition(right + 1, high)

        partition(0, len(nums) - 1)
        return nums
            