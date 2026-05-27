class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        
        mapping = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        if len(s)==0 or len(s)==1:
            return False

        for i in s:
            if i in "({[":
                l.append(i)
            
            elif i in "}])":
                if len(l)==0 or i!=mapping[l[-1]]:
                    return False
                l.pop()
        
        if len(l)==0:
            return True
        
        return False

        