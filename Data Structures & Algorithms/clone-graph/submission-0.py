"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        hashMap = {}
        cloneNode = Node(node.val)
        hashMap[node] = cloneNode
        visited = set()
        visited.add(node)
        
        def dfs(node: Optional['Node']) -> None:
            if not node:
                return
            for neighbor in node.neighbors:
                # A list of nodes where neighbor is a node
                if neighbor not in visited:
                    visited.add(neighbor)
                    cloneNode = Node(neighbor.val)
                    hashMap[neighbor] = cloneNode
                    hashMap.get(node).neighbors.append(cloneNode)
                    dfs(neighbor)
                else:
                    hashMap.get(node).neighbors.append(hashMap.get(neighbor))
        dfs(node)

        return hashMap[node]