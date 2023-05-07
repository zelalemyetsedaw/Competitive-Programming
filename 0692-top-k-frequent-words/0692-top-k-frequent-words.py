class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = defaultdict(int)
        heap = []
        
        for item in words:
            d[item] += 1
            
        for i,key in enumerate(d):
            heappush(heap,(-d[key],key))
            
        temp = nsmallest(k,heap)
        answer = []
        for item in temp:
            answer.append(item[1])
            
        return answer
        

            
            
            
            