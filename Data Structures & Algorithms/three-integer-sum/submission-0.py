# create a hashMap to check values that we have seen
# 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            seen = set()

            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = -(a + b)

                if c in seen:
                    res.add((a, b, c))
                seen.add(b)

        return list(res)