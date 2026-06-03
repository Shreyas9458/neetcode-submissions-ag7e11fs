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
            return node
        
        seen = dict()
        queue = deque([node])
        seen[node] = Node(node.val, [])

        while queue:
            currNode = queue.popleft()
            for nei in currNode.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val, [])
                    queue.append(nei)
                seen[currNode].neighbors.append(seen[nei])
        return seen[node]