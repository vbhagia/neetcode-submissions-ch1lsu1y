class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the array is sorted, we can use a 2 pointer approach
        # time: O(n), space: O(1)
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            if sum < target:
                l += 1
            if sum > target:
                r -= 1
        return False
            