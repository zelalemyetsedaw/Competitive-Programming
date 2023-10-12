class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        
        
        left, right = 0, len(self.d[key]) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2

            if self.d[key][mid][0] <= timestamp:
                result = self.d[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)