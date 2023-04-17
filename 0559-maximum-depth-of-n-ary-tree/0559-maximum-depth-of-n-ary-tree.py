"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        def dfs(root,cur,maxlen):
            if root == None:
                return maxlen
            
            maxlen = max(maxlen,cur)
            for child in root.children:
                maxlen = dfs(child,cur+1,maxlen)
                
            return maxlen
                
        return dfs(root,1,0)
        
            
            