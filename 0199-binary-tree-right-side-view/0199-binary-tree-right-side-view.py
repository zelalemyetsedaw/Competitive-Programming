# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        d = defaultdict(list)
        level = 0
        
        def preorder(root,level,d):
            
            if root == None:
                level -= 1
                return
            
            d[level].append(root.val)
            preorder(root.left,level+1,d)
            
            preorder(root.right,level+1,d)
         
        preorder(root,level,d)
        answer = []
        for item in d.values():
            answer.append(item[-1])
            
        return answer
            
            
        