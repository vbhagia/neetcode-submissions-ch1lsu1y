class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force. Time: O(n^2), Space: O(n)
        result = [0] * len(temperatures)
        print(result)
        for i in range(len(temperatures)):
            # find the next higher temp
            for j in range(i + 1, len(temperatures)):
                if result[i] == 0:
                    if temperatures[j] > temperatures[i]:
                        result[i] = j - i
                        print(f"{temperatures[j]} at {j} is greater than {temperatures[i]} at {i}")
                        print(result)
        print(f"checked {i}")
        return result

            
