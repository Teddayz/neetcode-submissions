class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_counts = len(nums1) + len(nums2)
        res = []
        end_count = 0
        isOdd = False
        if total_counts % 2 == 1:
            isOdd = True
            end_count = total_counts // 2 + 1
        else:
            end_count = total_counts // 2
        i, left, right = 0, 0, 0
        while i < end_count:
            if left >= len(nums1):
                res.append(nums2[right])
                right += 1
            elif right >= len(nums2):
                res.append(nums1[left])
                left += 1
            elif nums1[left] <= nums2[right]:
                res.append(nums1[left])
                left += 1
            else: 
                res.append(nums2[right])
                right += 1
            i += 1

        if isOdd:
            return res[-1]
        else:
            if left >= len(nums1):
                return (res[-1] + nums2[right]) / 2
            elif right >= len(nums2):
                return (res[-1] + nums1[left]) / 2
            elif nums1[left] <= nums2[right]:
                return (res[-1] + nums1[left]) / 2
            else:
                return (res[-1] + nums2[right]) / 2
                