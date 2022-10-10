"""Given the root of a Binary Search Tree and a target number k, return true if there exist two 
elements in the BST such that their sum is equal to the given target."""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dp = defaultdict(lambda:-1)
        def helper(root):
            if root==None:
                return False
            if dp[k-root.val]!=-1:
                return True
            dp[root.val]=1
            return helper(root.left) or helper(root.right)
        
        return helper(root)