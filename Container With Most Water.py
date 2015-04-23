class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        area, start, end = 0, 0, len(height) - 1
        while start < end:
            h = min(height[start], height[end])
            area = max(area, h*(end-start))
            if height[start] <= height[end]:
                ht = height[start]
                while True:
                    start+=1
                    if start == end or height[start] > ht:
                        break
            else:
                ht = height[end]
                while True:
                    end-=1
                    if start == end or height[end] > ht:
                        break
        return area