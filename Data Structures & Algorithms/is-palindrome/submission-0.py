class Solution:
    def isPalindrome(self, s: str) -> bool:

        # naive solution: flipping and checking if equal 

        s = s.lower()
        s = "".join(c for c in s if c.isalnum())


        flipped = "".join(reversed(s))

        return s == flipped
        