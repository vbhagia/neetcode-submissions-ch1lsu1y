class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # I think I should sort and then by adjusting 2 pointers for some fixed k (middle pointer)
        nums = sorted(nums)
        output = []
        
        # the fixed middle pointer should be applied to everything but the first and last elem
        for k in range(1, len(nums) - 1):
            # left and right pointers
            l = 0
            r = (len(nums) - 1)

            # don't worry about less or greater than 0 right now, just != 0.
            # optimize later, worry about O(n^2) now
            #try every l to the left of k, and every r to right right of k
            while l < k:
                while r > k:
                    sum = (nums[l] + nums[k] + nums[r])
                    if sum == 0:
                        if [nums[l], nums[k], nums[r]] not in output:
                            output.append([nums[l], nums[k], nums[r]])
                    r = r - 1
                l = l + 1
                # reset r
                r = (len(nums) - 1)
        
        return output
                    




