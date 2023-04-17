"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        sub = defaultdict(list)
        impo = defaultdict(int)
        
        for i in employees:
            sub[i.id] = i.subordinates
            impo[i.id] = i.importance
            
        total = impo[id]
        
        def dfs(lists,total):
            if lists == []:
                return total
            
            for item in lists:
                total += impo[item]
                total = dfs(sub[item],total)
                
            return total
        
        return dfs(sub[id],total)
        
        