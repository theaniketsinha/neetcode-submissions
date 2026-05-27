class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        i = 0
        j = l-1

        max_water = 0

        while i < j:
            water = min(heights[i],heights[j])* (j-i)
            max_water = max(max_water,water)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        
        return max_water