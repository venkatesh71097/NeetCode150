class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force O(n^2)
        # max_len = 0
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #     max_len = max(max_len, len(seen))
        # return max_len

        # Sliding window with optimization...
        seen_map = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in seen_map:
                l = max(l, seen_map[s[r]] + 1)
            seen_map[s[r]] = r
            max_len = max(max_len, r - l + 1)
        return max_len
        # Sliding window...
        # seen = set()
        # l = 0
        # max_len = 0 
        # for r in range(len(s)):
        #     while s[r] in seen and r < len(s):
        #         seen.remove(s[l])
        #         l = l + 1
        #     seen.add(s[r])
        #     max_len = max(r - l + 1, max_len)
        # return max_len