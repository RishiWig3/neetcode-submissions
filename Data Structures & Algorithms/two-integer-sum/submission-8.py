class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index in range(0, len(nums)):
            distance = target - nums[index]
            if nums[index] in mapping:
                return [mapping[nums[index]], index]
            if distance not in mapping:
                mapping[distance] =  index
            