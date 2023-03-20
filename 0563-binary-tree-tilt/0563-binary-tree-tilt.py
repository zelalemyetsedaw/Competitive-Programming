# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return (0, 0)

            leftsum= helper(root.left)
            rightsum = helper(root.right)

            rootsum = abs(leftsum[0] - rightsum[0])

            return (leftsum[0] + root.val + rightsum[0], 
                    leftsum[1] + rootsum + rightsum[1]) 
        
        return helper(root)[1]