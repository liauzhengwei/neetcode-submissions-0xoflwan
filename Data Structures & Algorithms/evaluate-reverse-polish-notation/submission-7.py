class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if token == "+":
                    result = num1 + num2  
                    stack.append(result)

                elif token == "*":
                    result = num1 * num2
                    stack.append(result)

                elif token == "/":
                    result = num2 / num1
                    stack.append(result)

                else:
                    result = num2 - num1
                    stack.append(result)

        return int(stack[-1])