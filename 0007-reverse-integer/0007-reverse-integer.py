class Solution:
    def reverse(self, x: int) -> int:
        def cal(s:int):
            s = str(x)
            if s[0]=='-':
                k=s[1:]
                return (0-int(k[::-1]))
                
            else:
                return (int(s[::-1]))

        if (x<=(2**31)-1) and (x>=(-2**31)):
            y = cal(x)
            if (y<=(2**31)-1) and (y>=(-2**31)):
                return y
            else:
                return 0
        else:
            return 0