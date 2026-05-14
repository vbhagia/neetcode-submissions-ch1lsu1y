class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Let's use a stack to keep track
        # of days still looking for a higher temp
        output = [0] * len(temperatures)
        stack = []
        
        # Push onto a stack until we find a higher val
        # Then we record the number of pops until we get there

        for i in range(len(temperatures)):
            cur_val = temperatures[i]
            
            while len(stack) > 0 and cur_val > stack[-1][0]:
                output[stack[-1][1]] = i - stack[-1][1]
                pop_it = stack.pop()

            stack.append([cur_val, i])
        
        return output