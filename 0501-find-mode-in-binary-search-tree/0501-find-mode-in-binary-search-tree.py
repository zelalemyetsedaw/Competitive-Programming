# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        
        def inorder(root):
            if root == None:
                return
            
            inorder(root.left)
            d[root.val] += 1
            inorder(root.right)
        
        inorder(root)
        maxvalue = max(d.values())
        answer = []
        
        
        if set(d.values()) == {maxvalue}:
            return list(d.keys())
        for key,count in d.items():
            if count == maxvalue:
                answer.append(key)
                
        return answer
                
            