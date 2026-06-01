class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        duplicateStatus = False
        for num in nums:
            if num in unique:
                duplicateStatus = True
            else:
                unique.add(num)
        return duplicateStatus