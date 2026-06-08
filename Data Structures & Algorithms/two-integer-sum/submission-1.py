class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1 

        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)): # for condition allows us to check every possibility
                if nums[i] + nums[j] == target:
                    return [i, j]


        # nums = [1,2,3,4]
        #target = 3
        # i = 0 
        # j = 1 
        # see if nums[0] + num[1] = 3 
        # if it does then return i and j 
        # if it doesn't then make j + 1 and once that is exhasuted make i + 1 
        