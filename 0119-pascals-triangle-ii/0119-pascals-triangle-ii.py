class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        array = self.getRow(rowIndex-1)
        
        final = [1]
        for i in range(1,len(array)):
            final.append(array[i-1] + array[i])
        final.append(1)
            
        return final
        
        
        
        
      
        
        
        
        
        