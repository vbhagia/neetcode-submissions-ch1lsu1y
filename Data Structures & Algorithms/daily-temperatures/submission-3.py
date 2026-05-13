class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ok let's literally brute force rn
        # O(n^2) kind of thing
        output = []
        for i in range(len(temperatures)):
            # find the num days to next highest temperature
            # if none, put 0
            appendme = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    appendme = j - i
                    break
            output.append(appendme)
        return output