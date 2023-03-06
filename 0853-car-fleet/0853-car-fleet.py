class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = [[p,s] for p,s in zip(position,speed)]
        array.sort(reverse = True)
        stack = []
        
        for p,s in array:
            temp = (target - p) / s
            if not stack:
                stack.append(temp)
            elif stack[-1] < temp:
                stack.append(temp)
        
        return len(stack)
        