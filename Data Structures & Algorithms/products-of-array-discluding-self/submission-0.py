class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # optimal 
        output = []
        prefix = []
        suffix = []
        val = 1

        for i in range(len(nums)):
            val *= nums[i]
            prefix.append(val)
        
        val = 1
        for j in range(len(nums) - 1, - 1, - 1):
            val *= nums[j]
            suffix.append(val)
        suffix.reverse()

        for k in range(len(nums)):
            left = prefix[k-1] if k > 0 else 1          # nothing to the left → 1
            right = suffix[k+1] if k < len(nums)-1 else 1  # nothing to the right → 1
            output.append(left * right)
        
        return output
        




        
        
        
        # integer array called nums 
        # return output array called output 
        # output[i] is product of all element sof nums except nums[i]

        # [1, 2, 3, 4]
        # i = 1 : 24
        # naive solution iterate over the array two times and compute the product 
        
        """
        output = [] 
        
        for i in range(len(nums)): # first loop is for keeping track of what we're looking at
            val = 1
            for j in range(len(nums)): 
                if j != i: 
                    val *= nums[j]  
            output.append(val)

        return output
        """

                






        