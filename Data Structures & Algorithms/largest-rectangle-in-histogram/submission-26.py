class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1

                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea