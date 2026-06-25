class Solution:
    def isPalindrome(self, s: str) -> bool:
        # optimal solution 2 pointers 

        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        i = 0 
        j = -1

        for i in range(len(s) // 2):
            if s[i] != s[j]:
                return False

            j -= 1
        
        return True
        
        
        
        
        
        
        
        # naive solution: flipping and checking if equal

        ''' 

        s = s.lower()
        s = "".join(c for c in s if c.isalnum())


        flipped = "".join(reversed(s))

        return s == flipped

        '''
        

