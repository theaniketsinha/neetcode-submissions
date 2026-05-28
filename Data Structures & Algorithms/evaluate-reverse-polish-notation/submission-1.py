class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:  
            if i in "+-*/":
                x = s.pop()
                y = s.pop()

                if i == '+':
                    s.append(x+y)
                elif i == '*':
                    s.append(x*y)
                elif i == '-':
                    s.append(y-x)
                elif i == '/':
                    s.append(int(y / x))
            else:
                s.append(float(i))
        
        return int(s[0])