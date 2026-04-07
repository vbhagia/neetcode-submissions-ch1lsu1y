class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1, count them all O(n)
        counted = dict()
        for num in nums:
            if num not in counted:
                counted[num] = 0
            counted[num] += 1
        # Step 2, find the top k and return
        output = []
        for x in range(k):
            # Find the highest val, add to output, remove corresponding key,val pair
            max_key = 0
            max_val = 0
            for key, val in counted.items():
                if val > max_val:
                    max_val = val
                    max_key = key
            output.append(max_key)
            del counted[max_key]
        return output