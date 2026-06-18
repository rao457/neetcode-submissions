class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            right_boundary = len(heights)
            if not stack:
                width = right_boundary
            else:
                width = right_boundary - stack[-1] - 1
            
            maxArea = max(maxArea, height*width)
        return maxArea