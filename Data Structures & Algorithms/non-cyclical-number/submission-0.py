class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = str(n)
        while True:
            sum = 0
            num = str(num)
            for i in range(len(num)):
                sum += int(num[i]) ** 2
            if sum in seen:
                return False
            if sum == 1:
                return True
            seen.add(sum)
            num = sum