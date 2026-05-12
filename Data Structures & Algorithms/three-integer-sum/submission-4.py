class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # I think we can just iterate through, and for each
        # look for a set of two others that give 0

        output = []

        # First I will sort the input, which will not increase time complexity
        # We are already dominated by the 2 pointer approach * n times.
        # Plus we sort in place, no extra memory
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Find 2 that add up to -i
            l = i + 1
            r = len(nums) - 1
            target = -1 * nums[i]
            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum == target:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                if cur_sum < target:
                    l += 1
                
                if cur_sum > target:
                    r -= 1
            
        return output