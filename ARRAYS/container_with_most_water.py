class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_water = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_water = max(area,max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
        
