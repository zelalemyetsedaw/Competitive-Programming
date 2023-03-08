# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = []
        
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            array.append(root.val)
            inorder(root.right)
            
        inorder(root)    
        for i in range(1,len(array)):
            if array[i] <= array[i-1]:
                return False
        return True