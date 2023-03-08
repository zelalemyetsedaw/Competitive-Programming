# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list) 
         
        def solv(node,row,col): 
            if not node: 
                return  
            store[col].append((row,node.val)) 
            left = solv(node.left,row+1,col-1) 
            right= solv(node.right,row+1,col+1) 
             
        solv(root,0,0) 
         
         
        answer = [] 
        storeColsSorted = sorted(store.keys()) 
        for col in storeColsSorted: 
            settedTupples =  sorted(store[col]) 
            temp = [] 
             
            for tuples in settedTupples: 
                temp.append(tuples[-1]) 
            answer.append(temp) 
         
        return answer