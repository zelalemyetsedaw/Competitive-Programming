class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        
        for i in matches:
            d[i[0]]=0
            d[i[1]]=0
            
        for i in matches:
            d[i[1]] += 1
            
        ans = [[],[]]
        
        for item,count in d.items():
            if count == 0:
                ans[0].append(item)
            elif count == 1:
                ans[1].append(item)
                
        ans[0].sort()
        ans[1].sort()
        
        return ans
                
            
            