class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers, where we modulate based on sum
        # This will be O(n) time and O(1) space
        l = 0
        r = len(numbers) - 1
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1