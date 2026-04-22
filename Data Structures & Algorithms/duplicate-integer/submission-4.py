# the problem is asking us to look through an array and see if any of the values
# appears more than once, and we return a boolean value if there is/isnt
# The naive way is to take the index of one calue and compare it to the rest of the values
# once that value is < 1, then return True. The issue is this would take N^2 or greater time 
# especially if any array is over 100 items

# the best solution is to pash through the array once and get every value inside
# a hashmap will help assign a key (the integer) and its corresponding value (count/occurance)
# once we have gotten all the value, if a number appears more than once then aha, duplicate

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #edge case: nums is empty
        if len(nums) == 0:
            return False 

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        