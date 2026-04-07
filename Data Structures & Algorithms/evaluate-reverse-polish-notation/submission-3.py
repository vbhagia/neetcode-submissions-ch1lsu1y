class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for token in tokens:
            print(stack)
            if token not in operators:
                stack = [int(token)] + stack
            else:
                b = stack.pop(0)
                a = stack.pop(0)
                print(f"doing {a} {token} {b}")
                if token == "+":
                    compute = a + b
                if token == "-":
                    compute = a - b
                if token == "*":
                    compute = a * b
                if token == "/":    
                    sign = 1
                    if (a > 0):
                        sign *= -1
                    if (b > 0):
                        sign *= -1
                    compute = sign*(abs(a)//abs(b))

                    
                
                stack = [compute] + stack
        
        return stack[0]

                