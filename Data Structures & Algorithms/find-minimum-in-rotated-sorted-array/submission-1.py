class Solution:
    def findMin(self, nums: List[int]) -> int:

        # naive: literally go one by one and update smaller 

        min = nums[0]

        for num in nums: 
            if num < min:
                min = num

        return min

        