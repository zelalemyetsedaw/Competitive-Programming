class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = defaultdict()
        n = len(names)
        for i in range(n):
            d[heights[i]] = names[i]
        for i in range(n):
            mini = i
            for j in range(i+1,n):
                if heights[mini]<heights[j]:
                    mini = j
            if i!=mini:
                heights[i],heights[mini] = heights[mini],heights[i]
        
        output = []
        for i in range(n):
            output.append(d[heights[i]])
        return output