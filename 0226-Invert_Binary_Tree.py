# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tree = TreeNode(root.val)
        if root.right:
            tree.left = self.invertTree(root.right)
        if root.left:
            tree.right = self.invertTree(root.left)
        return tree
