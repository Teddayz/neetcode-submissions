class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        
        start, end = -1, -1
        left, right = 0, 0
        hashMap_ref = Counter(t)
        curr_hashMap = {}

        while right < len(s):

            curr_hashMap[s[right]] = curr_hashMap.get(s[right], 0) + 1

            if self.isValidWindow(hashMap_ref, curr_hashMap):

                while left <= right and self.isValidWindow(hashMap_ref, curr_hashMap):
                    curr_hashMap[s[left]] -= 1
                    if curr_hashMap[s[left]] == 0:
                        curr_hashMap.pop(s[left])
                    left += 1

                # Now it is not a valid window
                left -= 1
                # Now it is a valid window
                currLength = right - left + 1
                if start == -1 or end == -1 or currLength < end - start + 1:
                    start = left
                    end = right
                left += 1
                
            right += 1

        if start == -1 or end == -1:
            return ""

        return s[start:end+1] 

    def isValidWindow(self, hashMap_ref, hashMap) -> bool:
        for key, value in hashMap_ref.items():
            if key not in hashMap or hashMap[key] < value:
                return False
        return True
                