class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Method 1: Brute force: O(n^2) - have the values in a set (so that the search is O(1) and not O(n))
        store = set(nums)
        max_streak = 0
        for n in nums:
            if (n-1) not in store:
                streak = 0
                curr = n
                while curr in store:
                    streak = streak + 1
                    curr = curr + 1
                max_streak = max(streak, max_streak)
        return max_streak

        # Method 2: 