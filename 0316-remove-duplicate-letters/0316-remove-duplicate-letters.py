class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        stack = []
        exist = defaultdict(bool)
        for i in set(s):
            exist[i] = False
        
        for item in s:
            if not stack:
                stack.append(item)
                freq[item] -= 1
                if freq[item] == 0:
                    freq.pop(item)
                exist[item] = True
            elif exist[item] == False and stack[-1] in freq and item < stack[-1] :
                while stack and stack[-1] in freq and item < stack[-1] :
                    exist[stack[-1]] = False
                    stack.pop()
                
                stack.append(item)
                freq[item] -= 1
                if freq[item] == 0:
                    freq.pop(item)
                exist[item] = True
                
                
                
            elif  item > stack[-1] and exist[item] == False:
                stack.append(item)
                exist[item] = True
                freq[item] -= 1
                if freq[item] == 0:
                    freq.pop(item)
                
            elif item < stack[-1] and exist[item] == False:
                stack.append(item)
                exist[item] = True
                freq[item] -= 1
                if freq[item] == 0:
                    freq.pop(item)
            else:
                freq[item] -=1
                if freq[item] == 0:
                    freq.pop(item)
                
        return "".join(stack)
                
            
        