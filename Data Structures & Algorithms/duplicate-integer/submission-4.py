class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        previous = nums[0]
        for count in range(1, len(nums)):
            if nums[count] == previous:
                return True
            else:
                previous = nums[count]
        return False