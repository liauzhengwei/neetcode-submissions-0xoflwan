class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
            # when the histogram goes down
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            # whenever, including when histogram goes up
            stack.append((start,h))

        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        # check the area from backwards
        return maxArea