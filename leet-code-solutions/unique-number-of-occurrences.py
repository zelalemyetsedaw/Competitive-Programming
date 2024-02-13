class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        d = defaultdict(int)
        for num in arr:
            d[num] += 1
        return len(d.values()) == len(set(d.values()))