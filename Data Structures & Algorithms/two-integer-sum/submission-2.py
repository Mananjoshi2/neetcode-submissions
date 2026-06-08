class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # make a hashmap 
        for i, num in enumerate(nums):
            complement = target - num 

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []






        # using a hashmap 
        # could look for complements 
        # each value has it as a key and a value of the complement 
        # for a cheap look up you can 


        # nums = [1,2,3,4]
        #target = 3
        # i = 0 
        # j = 1 
        # see if nums[0] + num[1] = 3 
        # if it does then return i and j 
        # if it doesn't then make j + 1 and once that is exhasuted make i + 1 
        