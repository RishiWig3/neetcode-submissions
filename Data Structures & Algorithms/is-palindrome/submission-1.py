class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s.lower() if ch.isalnum())
        for forwardIndex in range(0, len(s)):
            reverseIndex = (forwardIndex * -1) - 1
            if s[forwardIndex] != s[reverseIndex]:
                return False
        return True