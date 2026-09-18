class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I seem to remember a maxheap solution for this
        # I will stick to trying for an array/hashmap one right now
        # If we iterate through nums
        # And construct a hashmap of key: num, value: frequency
        # we can grab the k most frequent elements in O(n) time
        # This Solution is in O(n) time and space

        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Let's iterate over the dictionary k times
        # grab the top value's key,
        # and pop it.
        # Really slow and boring I know

        output = []
        
        for i in range(k):
            top_val = -9999
            top_key = ""
            for key, val in freq_map.items():
                if val > top_val:
                    top_val = val
                    top_key = key
            freq_map.pop(top_key)
            output.append(top_key)
        
        return output

                    
            
