class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = nums[0]            

        while low <= high:
            mid = (low + high) // 2
            res = min(res, nums[mid])  

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        return res               


        