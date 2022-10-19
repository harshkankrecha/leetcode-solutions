"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        mx=0
        
        def helper(root):
            nonlocal mx
            
            if root==None:
                return (0,0)
            
            ll,lr=helper(root.left)
            rl,rr=helper(root.right)
            l,r=0,0
            if root.left:
                if lr==0:l=1
                else:l=1+lr
            
            if root.right:
                if rl==0:r=1
                else:r=1+rl
            mx=max(mx,l,r)
            return (l,r)
        x=helper(root)
        return mx