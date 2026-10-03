class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hashSet = set(tuple(t) for t in triplets)
        if tuple(target) in hashSet:
            return True
        to_remove = []
        for i in range(len(triplets)):
            triplet = triplets[i]
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                to_remove.append(i)
        if to_remove:
            for index in reversed(to_remove):
                triplets.pop(index)

        if len(triplets) < 2:
            return False

        triplet = triplets[0]
        for i in range(1, len(triplets)):
            triplets[i] = [max(triplet[0], triplets[i][0]), max(triplet[1], triplets[i][1]), 
            max(triplet[2], triplets[i][2])]
            triplet = triplets[i]
        
        return triplets[len(triplets) - 1] == target
        