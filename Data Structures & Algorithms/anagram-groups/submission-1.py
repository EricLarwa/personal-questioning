# brrrattt brrratt
# all anagrams will be placed into their own list, 
# we could set a single string to a hashmap and compare each string to 
# the characters and their count, but this would be over O(n^2)

# we should take a single string and essentially make it a "key" for the other to compare to 
# as we move through the rest of the string 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        if len(strs) == 0:
            return results.add("")

        for string in strs:
            key = "".join(sorted(string))
            results[key].append(string)

        return list(results.values())
        