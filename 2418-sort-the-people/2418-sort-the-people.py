class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1,len(names)):
            key = heights[i]
            keys = names[i]
            j = i-1
            while j>=0 and heights[j]<key:
                
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -=1
            heights[j+1] = key
            names[j+1] = keys
                
                    
        
        return names
    
    