class Solution:
    def interpret(self, command: str) -> str:
        answer = []
        n = len(command)
        i = 0
        while i<n:
            if i+4 <= n and command[i:i+4] == '(al)':
                answer.append('al')
                i += 4
            elif i+2 <= n and command[i:i+2] == '()':
                answer.append('o')
                i += 2
            else:
                answer.append('G')
                i += 1
                
        return "".join(answer)