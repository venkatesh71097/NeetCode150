class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force...
        # area = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = max(area, (j - i) * min(heights[i], heights[j]))
        # return area
        # 2 ptrs
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            max_area = max(max_area, w * h)
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
        return max_area