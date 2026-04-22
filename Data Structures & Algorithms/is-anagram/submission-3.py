# asking if we have two strings that can be formed with the characters of the other
# checking around each character between the two strings would be exteremely slow
# we should keep a hash of ONE of the strings and compare the other one to see if all the characters that exists 
# in the hashmap of the first set.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case: two strings dont equal in length, cant make anagram
        if len(s) != len(t):
            return False

        seen = {}

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for char in t:
            if char not in seen:
                return False
            seen[char] -= 1

            if seen[char] < 0:
                return False

        return True


        