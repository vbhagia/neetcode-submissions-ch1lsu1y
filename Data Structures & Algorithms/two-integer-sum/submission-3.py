class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        seen = {}
        output = []
        for i in range(len(nums)):
            if target - nums[i] in seen:
                output.append(seen[target - nums[i]])
                output.append(i)
                return output
            seen[nums[i]] = i


        