class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = [(nums1[0] + nums2[0],0,0)]
        visited = set()
        answer = []
        i = 0
        while i<k and heap:
            x,y,z = heappop(heap)
            
            answer.append([nums1[y],nums2[z]])
            if y+1 < len(nums1) and (y+1,z) not in visited:
                heappush(heap,(nums1[y+1] + nums2[z],y+1,z))
                visited.add((y+1,z))
            if z+1 < len(nums2) and (y,z+1) not in visited:
                heappush(heap,(nums1[y] + nums2[z+1],y,z+1))
                visited.add((y,z+1))
            i+= 1
            
        return answer