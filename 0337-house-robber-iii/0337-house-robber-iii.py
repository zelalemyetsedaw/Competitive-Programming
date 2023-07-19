# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def postordertraversal(root):
            if root == None:
                return [0,0]
            
            left = postordertraversal(root.left)
            right = postordertraversal(root.right)
            
            node = root.val + left[1] + right[1]
            nonode = max(left) + max(right)
            return [node,nonode]
            
        return max(postordertraversal(root))