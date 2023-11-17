class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        busy = []
        freeroom = [i for i in range(n)]

        count = [0] * n
        meetings.sort()
        for start,end in meetings:

            while busy and busy[0][0] <= start:
                tempend,room = heapq.heappop(busy)
                heapq.heappush(freeroom,room)

            if freeroom:
                room = heapq.heappop(freeroom)
                heapq.heappush(busy,(end,room))

            else:
                endtime,room = heapq.heappop(busy)
                heapq.heappush(busy,(endtime + end-start,room))

            count[room] += 1

        return count.index(max(count))