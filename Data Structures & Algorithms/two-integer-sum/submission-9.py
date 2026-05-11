class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We will abuse the hashmap
        # This will give us a linear time solution,
        # With linear space consumption
        seen = dict()
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i