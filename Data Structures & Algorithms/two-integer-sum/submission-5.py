class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for countOne in range (len(nums)):
            for countTwo in range (countOne+1, len(nums)):
                if nums[countOne] + nums[countTwo] == target:
                    out = [countOne, countTwo]
                    break

        return out