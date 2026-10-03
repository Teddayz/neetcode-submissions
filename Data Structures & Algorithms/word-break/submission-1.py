class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        hashMap = {}

        def recursive_check(index: int) -> bool:
            if index == n:
                return True
            currWord = s[index:n+1]
            if currWord in hashMap:
                return hashMap[currWord]
            for word in wordDict:
                if currWord.startswith(word):
                    if recursive_check(len(word) + index):
                        return True
                hashMap[currWord] = False
            return False
        return recursive_check(0)

            