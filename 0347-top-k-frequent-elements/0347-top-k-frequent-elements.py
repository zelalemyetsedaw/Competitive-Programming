class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1 = defaultdict(int)
        for item in nums:
            dict1[item] += 1
        
        ans = []
        for key in dict1:
            ans.append((dict1[key],key))
            
        ans.sort(reverse=True)
        result = []
        
        if k>len(ans):
            k = len(ans)
        for i in range(k):
            result.append(ans[i][1])
            
        return result
            