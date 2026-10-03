class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        deadends = set(deadends)

        if "0000" in deadends:
            return -1
        
        frontier = deque()
        frontier.append(("0000", 0))

        visited = set()

        while frontier:
            curr, level = frontier.popleft()

            if curr == target:
                return level
                
            if curr in visited:
                continue
            visited.add(curr)

            for i in range(len(curr)):
                # Add 1 
                increase = str((int(curr[i]) + 1) % 10)
                str_to_add = curr[:i] + increase + curr[i + 1:]
                if str_to_add not in deadends and str_to_add not in visited:
                    frontier.append((str_to_add, level + 1))

                decrease = ""
                if curr[i] == "0":
                    decrease = "9"
                else:
                    decrease = str(int(curr[i]) - 1)
                str_to_add = curr[:i] + decrease + curr[i + 1:]
                if str_to_add not in deadends and str_to_add not in visited:
                    frontier.append((str_to_add, level + 1))
        return -1