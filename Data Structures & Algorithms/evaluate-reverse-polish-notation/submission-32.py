class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(token)

            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == "+":
                    result = num1 + num2

                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2

                else:
                    result = num1 / num2

                stack.append(result)

        return int(stack[-1])