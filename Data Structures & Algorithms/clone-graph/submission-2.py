class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Maps original nodes to their corresponding clones (also acts as our visited set)
        old_to_new = {}

        def dfs(curr: 'Node') -> 'Node':
            # If we've already cloned this node, return its clone from the map
            if curr in old_to_new:
                return old_to_new[curr]

            # Create the clone and store it immediately in the map
            clone = Node(curr.val)
            old_to_new[curr] = clone

            # Recursively clone all neighbors and attach them
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)