# create a pointer to check each index of the list
# as the pointer has compared two items, find a way to get the max value
# with the max value found, i need to find a minumum value that can fit water inside
# gain a total sum of the area between two values = amximum amt of water

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            area = width * height

            maxArea = max(maxArea, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        