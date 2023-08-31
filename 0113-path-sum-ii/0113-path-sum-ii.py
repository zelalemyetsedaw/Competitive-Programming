# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root,root.val,[root.val])]
        answer = []
        
        while stack:
            x , summ , temp = stack.pop()
            
            if summ == targetSum and not x.left and not x.right:
                answer.append(temp)
            
            if x.right:
                
                stack.append((x.right,summ + x.right.val,temp + [x.right.val]))
            
            if x.left:
                stack.append((x.left,summ + x.left.val,temp + [x.left.val]))
        return answer
            