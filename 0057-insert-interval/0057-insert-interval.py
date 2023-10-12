class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        answer = []
        intervals.append(newInterval)
        intervals.sort()
        answer.append(intervals[0])
        for b in intervals:
            p = answer.pop()
            if b[0] <= p[0] or b[0] <= p[1]:
                
                p = [min(b[0],p[0]),max(b[1],p[1])]
                
                answer.append(p)
            else:
                answer.append(p)
                answer.append(b)
                
        return answer
            