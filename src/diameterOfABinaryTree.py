# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0

            left_height = helper(node.left)
            right_height = helper(node.right)

            # Update the maximum diameter found so far
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return the height of the current subtree
            return 1 + max(left_height, right_height)

        self.max_diameter = 0
        helper(root)
        return self.max_diameter
