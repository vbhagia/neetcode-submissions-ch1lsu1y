class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        output = 0
        for num in numSet:
            curr_num = num
            curr_len = 1
            if (num - 1) not in numSet:
                #start here
                while (curr_num + 1) in numSet:
                    curr_num = curr_num + 1
                    curr_len = curr_len + 1
            if curr_len > output:
                output = curr_len
        return output
        