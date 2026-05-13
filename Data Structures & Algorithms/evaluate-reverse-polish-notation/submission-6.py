class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+','-','*','/']

        for token in tokens:
            if token not in operators:
                # Add to stack
                stack.append(int(token))
            
            if token in operators:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    answer = a + b
                if token == '-':
                    answer = a - b
                if token == '*':
                    answer = a * b
                if token == '/': 
                    answer = int(a / b)
                stack.append(answer)
        
        return stack.pop()
                    