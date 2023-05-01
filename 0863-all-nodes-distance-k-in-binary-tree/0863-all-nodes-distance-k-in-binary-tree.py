# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        if k==0:
            return [target.val]
        
        
        def findtarget(root):
            if root == None:
                return
            if not root.left and not root.right:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                
            findtarget(root.left)
            findtarget(root.right)
            
        findtarget(root)    
        
        queue = deque([target.val])
        visited = set([target.val])
        
        count = 0
        answer = []
        while queue:
            l = len(queue)
            count += 1
            
            for i in range(l):
                x = queue.popleft()
                for item in graph[x]:
                    if item not in visited:
                        visited.add(item)
                        queue.append(item)
                        if count == k:
                            answer.append(item)
            if count > k:
                break
                
        return answer

