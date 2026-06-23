class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # naive solution - for each one, just check if + 1 is in there or not and update counter until it isnt
        # optimal solution - create a hashmap with key and value of key + 1, counter of how many values are keys with values 


        longest = 0 # initialize if no consective sequence 

        nums = set(nums)
        for num in nums: 
            if num - 1 not in nums: 
                length = 1
                while num + 1 in nums:
                    num += 1
                    length += 1
                longest = max(longest, length)

        return longest



        