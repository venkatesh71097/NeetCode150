class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force... O(n^3 log n)
        # s1 = sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         substr = s2[i:j+1]
        #         substr = sorted(substr)
        #         if s1 == substr:
        #             return True
        # return False

        # Hashmap
        count1 = {} 
        for s in s1:
            count1[s] = count1.get(s, 0) + 1

        exp = len(count1)
        for i in range(len(s2)):
            count2 = {}
            cur_len = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if count2.get(s2[j]) > count1.get(s2[j], 0): 
                    break
                if count2[s2[j]] == count1.get(s2[j], 0):
                    cur_len += 1
                if cur_len == exp:
                    return True
        return False