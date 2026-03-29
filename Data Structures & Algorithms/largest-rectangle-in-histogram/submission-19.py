class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, width * height)

            stack.append(i)

        return maxArea