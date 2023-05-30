class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store5 = []
        store10 = []
        
        
        for i in bills:
            if i == 5:
                store5.append(5)
            elif i == 10:
                if not store5:
                    return False
                else:
                    store5.pop()
                    store10.append(10)
            else:
                if store5 and store10:
                    store5.pop()
                    store10.pop()
                    
                elif len(store5) >= 3:
                    store5.pop()
                    store5.pop()
                    store5.pop()
                else:
                    return False
        return True
                    