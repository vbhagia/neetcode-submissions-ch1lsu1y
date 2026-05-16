# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we can do this recursively
        node = root
        # Base case
        if node is None:
            return None


        # swap and recurse
        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        return node