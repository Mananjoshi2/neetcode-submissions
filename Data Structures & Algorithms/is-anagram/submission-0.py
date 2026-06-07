class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = ''.join(sorted(s.lower()))
        sorted_t = ''.join(sorted(t.lower()))

        if sorted_s != sorted_t:
            return False
        else: return True 



        