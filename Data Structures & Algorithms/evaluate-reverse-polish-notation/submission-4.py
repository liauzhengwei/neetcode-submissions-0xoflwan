class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    total = num1 + num2
                elif token == '*':
                    total = num1 * num2
                elif token == '-':
                    total = num2 - num1
                else:
                    total = int(num2 / num1)

                stack.append(total)

        return stack[0]