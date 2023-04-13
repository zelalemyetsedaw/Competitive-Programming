class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        node = set()
        answer = []
        for item in edges:
            node.add(item[1])
        
        for i in range(n):
            if i not in node:
                answer.append(i)
                
        return answer