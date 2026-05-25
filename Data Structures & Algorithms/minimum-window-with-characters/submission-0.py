class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_s = {}
        dict_t = {}
        if t == '':
            return ''

        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        have = 0
        need = len(dict_t)
        l = 0
        best_l = 0
        best_r = 0
        min_len = float('inf')
        for r in range(len(s)):
            dict_s[s[r]] = dict_s.get(s[r], 0) + 1
            if s[r] in dict_t and dict_s[s[r]] == dict_t[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    best_l = l
                    best_r = r
                    min_len = r - l + 1
                dict_s[s[l]] -= 1
                if s[l] in dict_t and dict_s[s[l]] < dict_t[s[l]]:
                    have -= 1
                l += 1
        return s[best_l:best_r + 1] if min_len != float('inf') else ''
            