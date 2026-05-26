class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all the non-alphanumeric characters from string
        s = "".join(char for char in s if char.isalnum())

        #calculate the length to be checked
        l = len(s) // 2
        
        #check till the length
        for i in range(l):
            if s[i].lower()!=s[-i-1].lower():
                return False
        
        return True