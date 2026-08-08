class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        result = []
        median_index = (m + n - 1) / 2
        # print(median_index)
        i = 0
        j = 0
        total = 0
        while total <= median_index:
            if i == m:
                result.append(nums2[j])
                j += 1
            elif j == n:
                result.append(nums1[i])
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else: 
                    result.append(nums2[j])
                    j += 1
            total += 1
        # print(total)
        if median_index != total - 1:
            next_number = 0
            if i == m:
                next_number = nums2[j]
            elif j == n:
                next_number = nums1[i]
            else:
                next_number = min(nums1[i], nums2[j])
            return (result[-1] + next_number) / 2

        return result[-1]