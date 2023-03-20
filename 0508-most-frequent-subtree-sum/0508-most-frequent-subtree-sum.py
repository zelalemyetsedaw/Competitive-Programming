# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            answer = root.val + l + r
            
            d[answer] += 1
            return answer
        
        d = collections.Counter()
        dfs(root)
        maximumvalue = max(d.values())
        return [i for i in d if d[i] == maximumvalue]