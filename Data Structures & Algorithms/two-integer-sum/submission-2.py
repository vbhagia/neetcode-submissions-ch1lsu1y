class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        output = []
        nums_dict = {}
        for i in range(0, len(nums)):
            if target - nums[i] in nums_dict:
                output.append(nums_dict[target - nums[i]])
                output.append(i)
                return output
            nums_dict[nums[i]] = i
            