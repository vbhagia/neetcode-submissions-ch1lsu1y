# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We have a helper function that takes the counter
        # and recurse
        depth = 0
        def deeper(root, depth):
            if root == None:
                return depth

            depth += 1
            return max(deeper(root.left, depth), deeper(root.right, depth))

        return deeper(root, depth)    