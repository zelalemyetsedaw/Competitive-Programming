# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        count = 0
        leftsum = defaultdict(int)
        leftsum[0] += 1
        
        stack = [(root,root.val,leftsum)]
        while stack:
            x,summ,leftsumm = stack.pop()
            
            
            if summ - targetSum in leftsumm:
                count += leftsumm[summ - targetSum]
            leftsumm[summ] += 1
            if x.right:
                stack.append((x.right,summ + x.right.val,leftsumm.copy()))
                
            if x.left:
                
                stack.append((x.left,summ + x.left.val,leftsumm.copy()))
            
                
        return count