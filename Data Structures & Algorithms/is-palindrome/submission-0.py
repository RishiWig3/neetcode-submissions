class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        backwardCount = len(s)-1
        for forwardCount in range(len(s)):
            if s[forwardCount] == s[backwardCount]:
                backwardCount -= 1
            else:
                return False
        return True