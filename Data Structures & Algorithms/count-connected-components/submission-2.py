class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return 0
            
            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return 1

        res = n
        for u, v in edges:
            res -= union(u, v)

        return res