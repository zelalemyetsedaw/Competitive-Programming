class Solution:
    def decodeString(self, s: str) -> str:
        
        def recursion(index,lists):
            if index == len(s):
                return lists
            if s[index] == "]":
                string = ""
                number = ""
                while lists and lists[-1] != "[":
                    string = lists.pop() + string
                lists.pop()
                while  lists and lists[-1].isdigit():
                    number = lists.pop() + number
                
                string = int(number) * string
                lists.append(string)
            else:
                lists.append(s[index])
            
            return recursion(index+1,lists)
            
        return "".join(recursion(0,[]))