# we need to check through the array and see where each number has apeared and keep a count of it
# a naive way would to be taking a simgle element and adding them until the match the target(k)
# the way i want to go about it, is to make a hashMap indicative of each number and its corresponding count
# later, we will compare the frequency of the number to the target and add it to a list
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if (len(result) == k):
                    return result

        