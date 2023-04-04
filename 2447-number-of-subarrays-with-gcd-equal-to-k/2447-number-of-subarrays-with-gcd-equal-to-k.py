class Solution:
    
    def gcd(self, a, b):
        
        if b == 0:
            return a
        return self.gcd(b , a % b)
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            currentgcd = 0
            
            for j in range(i , len(nums)):
                currentgcd = gcd(currentgcd, nums[j])
                
                if currentgcd == k:
                    count += 1
                    
        return count
            