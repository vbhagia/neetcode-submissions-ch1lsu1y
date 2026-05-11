class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # In total this approach takes O(n*log(n)) time, and O(n) space
        # First we need to know how frequent each elem is
        # Then, we need to get the top k most frequent elems

        # I think the first thing to do is make a hashmap consisting of:
        # Key: number, value: frequency
        # This frequency count will take O(n) time and space
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Now, we just sort by frequency into an array
        # Then we return the top k elems of the array
        # Sorting will take O(n*log(n)) time, and this will require O(n) space
        sorted_freq = []
        for key, value in freq.items():
            sorted_freq.append([value, key])
        # now sort this by val
        sorted_freq = sorted(sorted_freq, reverse=True)
        print(sorted_freq)
        
        out = []
        for subarray in sorted_freq[0:k]:
            out.append(subarray[1])
        
        return out