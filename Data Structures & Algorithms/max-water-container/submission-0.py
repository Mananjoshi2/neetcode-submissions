class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # naive: two for loops calculating each one
        # things to note: width increases with distance, and height is limited by the smaller one 

        # idea could start from opposite ends, max out the width , and bring it in based on what next height is bigger

        i, j = 0, len(heights) - 1
        maxWater = 0 

        while i < j: # we don't want them to cross
            length = min(heights[i], heights[j])
            width = j - i 
            area = (length*width)
            maxWater = max(maxWater, area)

            if min(heights[i], heights[j]) == heights[i]:
                i = i + 1

            else: 
                j = j - 1

        return maxWater




        