import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Quicksort -> Find a partition index, get all the values below this num is on the left and anything bigger will be put on the right
        def partition (low: int, high: int) -> None:

            if low >= high:
                return

            pivot = random.randint(low, high)
            nums[pivot], nums[high] = nums[high], nums[pivot] # Swap pivot with the last
            left = low - 1
            right = high
            middle = low - 1
            i = low
            target = nums[high]
            while i < right:
                if nums[i] < target:
                    left += 1
                    nums[left], nums[i] = nums[i], nums[left]
                    middle += 1
                    i += 1
                elif nums[i] > target:
                    right -= 1
                    nums[i], nums[right] = nums[right], nums[i]
                else:
                    middle += 1
                    nums[i], nums[middle] = nums[middle], nums[i]
                    i += 1
            nums[right], nums[high] = nums[high], nums[right]
            partition(low, left)
            partition(right + 1, high)

        partition(0, len(nums) - 1)
        return nums                
