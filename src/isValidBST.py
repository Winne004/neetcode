# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root): 
            if not root:
                return None

            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                return left < root.val < right  
            if left:
                return left < root.val 
            if right:
                return root.val < right 
            
            else: 
                return root.val 

        return helper(root)
    

root = TreeNode(1,TreeNode(0),TreeNode(2))
root2 = TreeNode(0 )
c = Solution()
print(c.isValidBST(root2))