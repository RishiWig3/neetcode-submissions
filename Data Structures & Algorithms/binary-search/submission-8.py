class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        found = False
        rangeLow = 0
        rangeHigh = len(nums)-1

        while found == False:
            if (nums[rangeLow] == target):
                return rangeLow
            if (nums[rangeHigh] == target):
                return rangeHigh
            if (rangeHigh - rangeLow) <= 1:
                return index
            avg = int((rangeLow + rangeHigh) / 2)
            if nums[avg] == target:
                index = avg
                found = True
            elif nums[avg] > target:
                rangeHigh = avg
            elif nums[avg] < target:
                rangeLow = avg
        return index 