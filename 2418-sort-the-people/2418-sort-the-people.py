class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
       
        n = len(names)
        
        for i in range(n):
            mini = i
            for j in range(i+1,n):
                if heights[mini]<heights[j]:
                    mini = j
            if i!=mini:
                heights[i],heights[mini]= heights[mini],heights[i]
                names[i],names[mini] = names[mini],names[i]
        
        
        return names