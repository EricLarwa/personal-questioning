# asking us to get the product of each number as we increment, 
# since we are getting the product of every number it is the perfect time to use prefix sum :D
# set a prefix to an empty array and populate the output into an empty array
# after that we have kinda, exactly what we need 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        