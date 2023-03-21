# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        cur = ""
        def helper(root,cur):
            if root == None:
                return
            if root.left == None and root.right == None:
                cur += str(root.val)
                ans.append(cur)
            
            cur += str(root.val) + "->"
            helper(root.left,cur)
            helper(root.right,cur)
            
            
            
        helper(root,cur)
        return ans
            
            