class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.tree = defaultdict(list)
        self.tree[kingName]=list()
        self.kingName = kingName
        self.deathset = set()
    
    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deathset.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        answer = []
        if self.kingName not in self.deathset:
            answer = [self.kingName]
        def dfs(temp):
            if temp not in self.tree:
                return
            
            for child in self.tree[temp]:
                if child not in self.deathset:
                    answer.append(child)
                dfs(child)
        
        
        dfs(self.kingName)
        return answer
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()