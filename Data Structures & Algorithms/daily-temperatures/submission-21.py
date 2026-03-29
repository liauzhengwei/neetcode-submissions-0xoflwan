class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = n * [0]

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res