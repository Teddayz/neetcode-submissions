class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        minSteps = 0
        adjList = defaultdict(list) # Maps patterns to words

        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i+1:]
                adjList[pattern].append(word)
        
        frontier = deque()
        frontier.append((beginWord, 1))
        visited = set()
        while frontier:
            currTuple = frontier.popleft()
            currWord = currTuple[0]
            level = currTuple[1]
            if currWord == endWord:
                return level
            # If we have seen this word before (prevent infinite loops)
            if currWord in visited:
                continue

            visited.add(currWord)
            children = self.getPatterns(currWord)
            for child in children:
                wordsToCheck = adjList.get(child, [])
                for word in wordsToCheck:
                    if word not in visited:
                        frontier.append((word, level + 1))

        return 0


    def getPatterns(self, word: str) -> List[str]:
        result = []
        for i in range(len(word)):
            pattern = word[0:i] + "*" + word[i+1:]
            result.append(pattern)
        return result
        