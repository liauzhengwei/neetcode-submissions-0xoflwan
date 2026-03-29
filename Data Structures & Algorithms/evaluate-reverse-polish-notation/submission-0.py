class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                
                if token == '+':
                    result = first + second
                elif token == '-':
                    result = second - first
                elif token == '/':
                    result = int(second / first)
                elif token == '*':
                    result = second * first
                
                stack.append(result)

        return stack.pop()