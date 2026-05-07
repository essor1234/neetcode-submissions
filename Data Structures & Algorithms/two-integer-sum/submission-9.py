class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i in range(len(nums)):
            cal = target - nums[i]
            if cal in seen:
                return [seen[cal], i]

            seen[nums[i]] = i

        return []