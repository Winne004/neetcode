# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_val):
            if not node:
                return 0
            
            max_val = max(max_val, node.val)

            left_count = helper(node.left, max_val)
            right_count = helper(node.right, max_val)

            return left_count + right_count + (node.val >= max_val)

        return helper(root, float('-inf'))