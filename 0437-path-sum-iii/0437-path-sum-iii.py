# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dicts = defaultdict(int)
        dicts[0] = 1
        summ = 0
        count = 0
        def findsum(root,targetsum,summ,count):
            if root == None:
                return count,summ
            
            summ += root.val
            if summ-targetsum in dicts:
                count += dicts[summ-targetsum]
            
            dicts[summ] += 1
            count,summ = findsum(root.left,targetsum,summ,count)
            count,summ = findsum(root.right,targetsum,summ,count)
            dicts[summ] -= 1
            summ -= root.val
            
            
            
            return count,summ
        
        count,summ =  findsum(root,targetSum,summ,count)
        return count
            
            