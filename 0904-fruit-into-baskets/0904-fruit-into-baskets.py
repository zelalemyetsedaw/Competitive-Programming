class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        dicts = defaultdict(int)
        maxlen = 0
        for right in range(len(fruits)):
            dicts[fruits[right]] += 1
            while len(dicts) > 2:
                dicts[fruits[left]] -= 1
                if dicts[fruits[left]] == 0:
                    dicts.pop(fruits[left])
                left += 1
                
            maxlen = max(maxlen,right-left + 1)
            
        return maxlen
            