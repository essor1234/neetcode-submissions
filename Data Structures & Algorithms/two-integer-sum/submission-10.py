class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            cal = target - num
            if cal in seen:
                return [seen[cal], i]

            seen[num] = i

        return []