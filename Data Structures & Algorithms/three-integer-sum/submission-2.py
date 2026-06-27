class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # naive triple nested for loop On^3
        # optimal sort + 2 pointers
        result = [] # output
        nums.sort() # sort first

        for i, a in enumerate(nums): # key and values
            if i > 0 and a == nums[i - 1]:  # if the previous same, move on
                continue
            l = i + 1  # pointer at beginning 
            r = len(nums) - 1 # pointer at the end 
            while l < r:  # l and r can't be equal
                sum = a + nums[l] + nums[r] # check sum
                if sum > 0:  # if sum too big, make r smaller
                    r -= 1
                elif sum < 0:  # if sum too lil make l bigger
                    l += 1
                else:  # it is zero to append and move l once
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # skip duplicates of l to find the next one
                        l += 1
        return result

                






        