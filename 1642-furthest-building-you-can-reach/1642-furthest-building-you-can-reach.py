class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        difference = []
        heap = []
        for i in range(1,len(heights)):
            difference.append(heights[i]-heights[i-1])
        
        
        for i in range(len(difference)):
            
            if difference[i] > 0 and bricks-difference[i]>=0:
                
                heappush(heap,-difference[i])
                bricks -= difference[i]
            elif difference[i] > 0 and bricks-difference[i] < 0 and ladders>0:
                
                if heap:
                    x = -heappop(heap)
                    
                    if x > difference[i]:
                        heappush(heap,-difference[i])
                        bricks += x-difference[i]
                    else:
                        heappush(heap,-x)
                ladders -= 1
            
            elif difference[i] > 0 and ladders == 0 and bricks-difference[i] < 0:
                return i
                    
        return len(heights)-1
                    
                    
                
                
                
            