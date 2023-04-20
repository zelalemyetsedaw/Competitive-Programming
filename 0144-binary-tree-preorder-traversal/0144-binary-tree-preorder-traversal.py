# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        def preorderTraversal(root):
            if root == None:
                return 

            answer.append(root.val)
            preorderTraversal(root.left)
            preorderTraversal(root.right)
        
        preorderTraversal(root)
        return answer