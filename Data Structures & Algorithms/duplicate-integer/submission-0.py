class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for value in nums:
            if (value not in unique):
                unique.append(value)
            else:
                return True
        return False