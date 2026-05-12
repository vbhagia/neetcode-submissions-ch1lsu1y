class Solution:
    def isValid(self, s: str) -> bool:
        # We simply place each open char on the stack
        # Remove when is top of stack, and corresponding close char appears
        # Error if wrong close appears
        # Error if stack not empty when finished

        stack = []
        
        openers = ['(', '[', '{']
        closers = [')', ']', '}']
        for char in s:
            if char in openers:
                stack.append(char)
            elif char in closers:
                i = closers.index(char)
                if len(stack) < 1:
                    return False
                top = stack.pop()
                if top != openers[i]:
                    return False
        if stack != []:
            return False
        return True
                

            