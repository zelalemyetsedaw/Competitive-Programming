class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = defaultdict()
        n = len(names)
        for i in range(n):
            d[heights[i]] = names[i]
        for i in range(n):
            for j in range(n-1):
                if heights[i]>heights[j]:
                    heights[i],heights[j] = heights[j],heights[i]
        
        for i in range(n):
            names[i] =d[heights[i]]
        return names