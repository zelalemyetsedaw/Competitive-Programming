class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left = 0
        right = 1
        count = 1
        chars.append(" ")
        
        while right < len(chars):
            if chars[right] == chars[right-1]:
                count += 1
            else:
                if count == 1:
                    chars[left] = chars[right-1]
                    count = 1
                elif count > 1 and count < 10:
                    chars[left] = chars[right-1]
                    left = left+1
                    
                    chars[left] = str(count)
                    count = 1
                else:
                    chars[left] = chars[right-1]
                    count = str(count)
                    for i in range(len(count)):
                        left += 1
                        chars[left] = count[i]
                        
                        
                    count = 1
                left += 1
            right += 1
                
        return left
                
        
                    
            
            