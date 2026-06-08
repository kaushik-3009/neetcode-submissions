class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow, fast = 0, len(heights)-1

        best_area = 0

        while slow<fast:
            if heights[slow]<= heights[fast]:
                best_area = max(best_area, heights[slow]*(fast-slow))
                slow+=1
            else:
                best_area = max(best_area, heights[fast]*(fast-slow))
                fast-=1

        return best_area