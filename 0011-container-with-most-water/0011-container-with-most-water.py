class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0 
        left = 0 
        right = len(height)-1
        while left < right: 
            volume = max(
                volume,
                min(height[left], height[right]) * (right - left)
            )
            
            if height[left] >= height[right]:
                right -= 1 
            else:
                left += 1
        
        return volume

        