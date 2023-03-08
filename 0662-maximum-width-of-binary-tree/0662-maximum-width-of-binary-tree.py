# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        level = 0
        position = 0
        
        def preorder(root,level,position):
            
            if root == None:
                
                level -= 1
                return
            
            
            d[level].append(position)
            preorder(root.left,level+1,position * 2)
            
            preorder(root.right,level+1,position * 2 + 1)
         
        preorder(root,level,position)
        
        maxvalue = -1
        for item in d.values():
            maxvalue = max(maxvalue,item[-1] - item[0] + 1)
            
        return maxvalue
            
        