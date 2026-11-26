"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}

        def dfs(curr: Optional['Node']) -> Optional['Node']:
            if curr in old_to_new:
                return old_to_new[curr]
            
            clone = Node(curr.val)
            old_to_new[curr] = clone

            for neighbour in curr.neighbors:
                clone.neighbors.append(dfs(neighbour))

            return clone

        return dfs(node)