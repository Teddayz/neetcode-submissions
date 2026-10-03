class CountSquares:

    def __init__(self):
        self.hashMap = {}

    def add(self, point: List[int]) -> None:
        self.hashMap[tuple(point)] = self.hashMap.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        for p, freq in self.hashMap.items():
            if self.absolute_distance(point, p) == 0:
                # print(point, p)
                diagonal = p
                curr = self.hashMap[p]
                if tuple([p[0], point[1]]) in self.hashMap and tuple([point[0], p[1]]) in self.hashMap:    
                    curr = max(curr, curr * self.hashMap[tuple([p[0], point[1]])])
                    curr = max(curr, curr * self.hashMap[tuple([point[0], p[1]])])
                    res += curr
        return res


    def absolute_distance(self, point1: List[int], point2: List[int]) -> int:
        if point1[0] == point2[0] and point1[1] == point2[1]:
            return -1
        return abs(point1[0] - point2[0]) - abs(point1[1] - point2[1])
        
