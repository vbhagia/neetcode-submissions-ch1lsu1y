import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We will use a hashmap to track frequency
        # Then a minheap to grab the k most frequent elems

        # 1. Construct hashmap
        # This will take O(n) space and time
        # key: num, value: frequency
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # 2. minheap time.
        # We only need to maintain a minheap of size k,
        # This keeps the k most frequent elems in nums
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
