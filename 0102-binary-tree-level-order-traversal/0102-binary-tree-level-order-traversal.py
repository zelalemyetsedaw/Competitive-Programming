# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        level = 0
        
        def preorder(root,level):
            
            if root == None:
                level -= 1
                return
            
            d[level].append(root.val)
            preorder(root.left,level+1)
            
            preorder(root.right,level+1)
         
        preorder(root,level)
        return list(d.values())