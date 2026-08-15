# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def maxDepth(root):
            nonlocal d
            if not root:
                return 0
            
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            d = max(d, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        maxDepth(root)
        return d