class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = dict()
        for num in nums:
            if num not in counted:
                counted[num] = 0
            counted[num] += 1
        output = []
        for x in range(k):
            # Find the highest value
            # add it's key to output
            # remove the key from counted
            max_key = 0
            max_val = 0
            for key, val in counted.items():
                if val > max_val:
                    max_val = val
                    max_key = key
            output.append(max_key)
            del counted[max_key]
        return output