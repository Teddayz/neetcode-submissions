class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        inDegree = {}
        adjList = defaultdict(list)
        unique_characters = {char for word in words for char in word}
        if len(words) == 1:
            return words[0]
        result = ""

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            l1 = len(word1)
            l2 = len(word2)
            min_len = min(l1, l2)
            if l1 > l2 and word1[:min_len] == word2[:min_len]:
                return ""
            for index in range(min_len):
                if word1[index] != word2[index]:
                    adjList[word1[index]].append(word2[index])
                    inDegree[word2[index]] = inDegree.get(word2[index], 0) + 1
                    break

        queue = []
        for char in unique_characters:
            if char not in inDegree:
                inDegree[char] = 0
        for k, v in inDegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            letter = queue.pop(0)
            if letter in result:
                continue
            result += letter
            neighbours = adjList.get(letter, [])
            for neighbour in neighbours:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

        return "".join(result) if len(unique_characters) == len(result) else ""