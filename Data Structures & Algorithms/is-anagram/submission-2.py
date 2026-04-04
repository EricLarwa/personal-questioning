# an anagram holds the same amount of characters in a string, 
# if the strings do not match, then false

# we want to see if the two strings CONTAIN the same characters to be anagrams,
# a poorly executed method would be to run a nested loop over each string and compare the values,
# at each index that has been seen. 

# the quickest way to go about this is to set a dictionary for each string
# the dictionary will allow us to check if there is a character (and frequency of character) 
# apart of either string, that matches the other

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # test case: lengths not match 
        if len(s) != len(t):
            return False

        # empty dictionary time :D 
        CountS, CountT = {}, {}
        
        # we can loop over the length of one string, since both lengths are the same
        for i in range(len(s)):
            # get the character at each index, put it into the ditionary
            # add 0 if not already seen, add 1 otherwise
            CountS[s[i]] = CountS.get(s[i], 0) + 1
            CountT[t[i]] = CountT.get(t[i], 0) + 1

        # returh if everything matches
        return CountS == CountT



        