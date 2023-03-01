class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts2 = defaultdict(int)
        left = 0
        right = 0
        count = 0
        
        for right in range(len(fruits)):
            counts2[fruits[right]] += 1
            while len(counts2) > 2:
                counts2[fruits[left]] -= 1
                if counts2[fruits[left]] == 0:
                    counts2.pop(fruits[left])
                left += 1
            count = max(count,right-left+1)
            
            
        return count
        
            
            
            