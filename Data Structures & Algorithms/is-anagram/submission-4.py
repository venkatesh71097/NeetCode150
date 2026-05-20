class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If case insensitive, you can do a .lower() for both strings...
        
        # Route 1 - Counter: 
        # from collections import Counter
        # return Counter(s) == Counter(t)

        # Route 2 - Dict tracking: 
        # if len(s) != len(t):
        #     return False
        # d1 = {}
        # d2 = {}
        # for x, y in zip(s, t):
        #     d1[x] = d1.get(x, 0) + 1
        #     d2[y] = d2.get(y, 0) + 1
        # return d1 == d2

        # Route 3: Single dict
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        for val in count.values():
            if val != 0:
                return False
        return True