class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # naive going through every element 
        # optimal binary search

        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid

            if nums[mid] >= nums[l]:     # left half is sorted
                if nums[mid] > target >= nums[l]:
                    r = mid - 1          # target is in left half
                else: 
                    l = mid + 1          # target is in right half
            
            else:                        # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid  + 1         # target is in right half
                else: 
                    r = mid - 1          # target is in left half

        return -1  



        