class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: 
            if num in seen:
                return True 
            seen.add(num)

        return False
        



        #nums = [1,2,3,4,5]
        #true if any value in the nums appears twice 
        #false if every is distinct