class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for letter in s:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1
        dict2 = {}
        for letter in t:
            if letter in dict2:
                dict2[letter] += 1
            else:
                dict2[letter] = 1
        if dict1 == dict2:
            return True
        else:
            return False


        # Problem:
        #     two strings
        #     load first into first dictionary -> O(n) time
        #     load second into second dictionary -> O(m) time
        #     compare values at end -> O(n) time
        # SIZE: O(n+m) space.

        