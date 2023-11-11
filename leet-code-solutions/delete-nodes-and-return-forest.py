# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        answer = []
        todelete = set(to_delete)
        def dfs(root,flag):
            if not root:
                return
            if root.val in todelete:
                root.left = dfs(root.left,True)
                root.right = dfs(root.right,True)
                return None
            else:
                if flag:
                    answer.append(root)

                root.left = dfs(root.left,False)
                root.right = dfs(root.right,False)
                return root
        
        dfs(root,True)
        return answer
