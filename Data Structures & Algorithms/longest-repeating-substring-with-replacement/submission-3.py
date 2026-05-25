class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0
        max_freq = 0
        max_len = 0
        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(max_freq, freq_map[s[r]])

            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l = l + 1
            max_len = max(max_len, r - l + 1)
        return max_len