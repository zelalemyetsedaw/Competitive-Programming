class DetectSquares:

    def __init__(self):
        self.array = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.array[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        dx,dy = point[0],point[1]
        ans = 0
        temp = self.array.copy()
        for x,y in temp.keys():
            
            if abs(dx-x) == abs(dy-y) and dx != x and dy != y:
                               
                ans += self.array[(dx,y)] * self.array[(x,dy)] * self.array[(x,y)]
        return ans

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)