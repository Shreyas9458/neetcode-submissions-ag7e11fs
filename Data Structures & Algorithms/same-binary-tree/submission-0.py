# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not (p and q):
            return False
        queue = deque()
        queue.append([p, q])
        
        while queue:
            pNode, qNode = queue.popleft()

            if pNode.val == qNode.val:
                if pNode.left and qNode.left:
                    queue.append([pNode.left, qNode.left])
                if pNode.right and qNode.right:
                    queue.append([pNode.right, qNode.right])
                if pNode.left and not qNode.left:
                    return False
                if pNode.right and not qNode.right:
                    return False
                if not pNode.left and qNode.left:
                    return False
                if not pNode.right and qNode.right:
                    return False
            else:
                return False
        return True
        