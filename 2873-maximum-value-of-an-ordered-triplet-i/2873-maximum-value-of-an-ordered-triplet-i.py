class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        
        
        maxansweruntilnow = maxdifferenceuntilnow = maxnumberuntilnow = 0
        for item in nums:
            maxansweruntilnow = max(maxansweruntilnow, maxdifferenceuntilnow * item)
            maxdifferenceuntilnow = max(maxdifferenceuntilnow, maxnumberuntilnow - item)
            maxnumberuntilnow = max(maxnumberuntilnow,item)
            
        return maxansweruntilnow
                            
                            
                        
                        
                    