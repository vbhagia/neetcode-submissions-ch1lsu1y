class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force solution (O(n^2))
        output = []
        for i in range(len(nums)):
            product_x_self = 1
            for j in range(len(nums)):
                if i != j:
                    product_x_self *= nums[j]
            output.append(product_x_self)
        return output